# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/02_train.ipynb.

# %% auto 0
__all__ = ['xgb_trainer']

# %% ../nbs/02_train.ipynb 4
def xgb_trainer(df,
                feature_col,
                target_col,
                test_index=None,
                xgb_params = { 
                            'max_depth':7, #from 4 to 7
                            'learning_rate':0.001, #from 0.001
                            'subsample':0.8,
                            'colsample_bytree':0.2, # from 0.2 to 1, because need to take position
                            'eval_metric':'rmse',
                            'objective':'reg:squarederror',
                            'tree_method':'gpu_hist',
                            'predictor':'gpu_predictor',
                            'random_state':123
                        }
               ):
    
    X = df[feature_col]
    y = df[target_col]
    
    print(f'xgb params is: {xgb_params}')
    
    if test_index is None:
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123)
    else:
        X_train,y_train = X.loc[~X.index.isin(test_index)],y.loc[~X.index.isin(test_index)]
        X_test, y_test = X.loc[test_index],y.loc[test_index]

        
    print(X_train.shape,y_train.shape,X_test.shape, y_test.shape)
    print(y_test.index)
    #prepare matrix for xgb
    dtrain = xgb.DMatrix(X_train, y_train)
    dtest = xgb.DMatrix(X_test, y_test)
    
    model = xgb.train(xgb_params, 
            dtrain=dtrain,
            evals=[(dtrain,'train'),(dtest,'valid')],
            num_boost_round=9999,
            early_stopping_rounds=100,
            verbose_eval=100,)
    
    pred = model.predict(dtest)
    spearman_corr, _ = spearmanr(y_test, pred)
    print(f'Spearman correlation: {spearman_corr:.2f}')
    
    fig, ax = plt.subplots()
    ax.scatter(y_test, pred)
    ax.set_xlabel('True values')
    ax.set_ylabel('Predicted values')
    ax.set_title('Scatter plot of true versus predicted values')
    plt.show()
    plt.close()
    
    
    dd = model.get_score(importance_type='gain')
    gain = pd.DataFrame({'feature':dd.keys(),f'gain_importance':dd.values()})
    gain.set_index('feature').sort_values(by = 'gain_importance')[:15].plot.barh(figsize=(10,20))
    plt.show()
    plt.close()
    
        
    dd = model.get_score(importance_type='weight')
    weight = pd.DataFrame({'feature':dd.keys(),f'weight_importance':dd.values()})
    weight.set_index('feature').sort_values(by = 'weight_importance')[:15].plot.barh(figsize=(10,20))
    plt.show()
    plt.close()
    
    return gain, weight
