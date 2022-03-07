import numpy as np
from sklearn.linear_model import RidgeCV
import statsmodels.api as sm
from sklearn.metrics import r2_score

def regress(df, xcols, ycol, steps=500):
    """
    This function runs the regression
    :param df: standardized df
    :param xcols: name of independent features
    :param ycol: name of y col
    :return: dictionary of regression results
    """

    df_r = df.copy()

    # ridge bootstrap
    ridge_bootstrap = Bootstrap(X=df_r[xcols].values, y=df_r[ycol].values, model=RidgeCV(alphas=np.logspace(-1, 1, 30)), steps=500, features=xcols)
    ridge_bootstrap.bootstrap()

    # OLS
    model = sm.OLS(df_r[ycol].values, sm.add_constant(df_r[xcols]))
    results = model.fit()

    results_dict = {"Ridge": ridge_bootstrap,
                    "OLS": {"aic": results.aic, "r2": results.rsquared,
                            "params": results.params, "CI": results.conf_int()}}
    return results_dict


def AIC(y_true, y_pred, k):
    """
    This function compute the Akaike Information Criterion
    (emulates statsmodel implementation: https://www.statsmodels.org/dev/_modules/statsmodels/regression/linear_model.html#RegressionResults.aic)
    """
    nobs2 = len(y_true) / 2.0
    y_true, y_pred = np.array(y_true), np.array(y_pred)

    SSR = np.sum((y_true - y_pred) ** 2)
    llf = -np.log(SSR) * nobs2  # concentrated likelihood
    llf -= (1 + np.log(np.pi / nobs2)) * nobs2  # with likelihood constant
    return 2 * k - 2 * llf


class Bootstrap():
    """
    Bootstrap Class
    # https://machinelearningmastery.com/a-gentle-introduction-to-the-bootstrap-method/
    """

    def __init__(self, X, y, model, steps, features):
        self.model = model
        self.X = np.array(X)
        self.y = np.array(y)
        self.n = self.y.shape[0]
        self.steps = steps
        self.features = features
        self.params = {f: np.zeros(self.steps) for f in features}
        self.r2_train = np.zeros(self.steps)
        self.r2_test = np.zeros(self.steps)
        self.aic_train = np.zeros(self.steps)
        self.aic_test = np.zeros(self.steps)
        self.alpha = np.zeros(self.steps)

    def resample(self):
        """
        Resample with replacement
        """
        idx = np.random.choice(self.n, self.n, replace=True)
        oob_idx = [i for i in range(self.n) if i not in idx]
        return self.X[idx], self.y[idx], self.X[oob_idx], self.y[oob_idx]

    def bootstrap(self):
        """
        Bootsrap regression
        """
        for s in range(self.steps):
            # resample
            X_r, y_r, X_oob, y_oob = self.resample()
            clf = self.model.fit(X_r, y_r)
            for i in range(len(self.features)):
                self.params[self.features[i]][s] = clf.coef_[i]
            self.alpha[s] = clf.alpha_
            self.r2_train[s] = r2_score(y_r, clf.predict(X_r))
            self.r2_test[s] = r2_score(y_oob, clf.predict(X_oob))
            self.aic_train[s] = AIC(y_r, clf.predict(X_r), X_r.shape[1])
            self.aic_test[s] = AIC(y_oob, clf.predict(X_oob), X_oob.shape[1])