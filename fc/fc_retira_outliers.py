import numpy as np

def retira_outliers(dfx):
    column_names = list(dfx)
    conta_out = 1

    while conta_out > 0:
        conta_out = 0

        for names in column_names[1:]:
            for x in [names]:

                q75,q25 = np.percentile(dfx.loc[:,x],[75,25])
                intr_qr = q75-q25

                max = q75+(1.5*intr_qr)
                min = q25-(1.5*intr_qr)

                dfx.loc[dfx[x] < min,x] = np.nan
                dfx.loc[dfx[x] > max,x] = np.nan

                conta_out += dfx.loc[dfx[x] < min,x].count() + dfx.loc[dfx[x] > max,x].count()

                dfx = dfx.dropna(axis = 0)
            
    return dfx