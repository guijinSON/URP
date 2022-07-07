import talib

def overlapStudies(open_, high, low, close, volume):
    # Bollinger Bands
    bbands = talib.BBANDS(close, timeperiod=5, nbdevup=2, nbdevdn=2, matype=0)
    # Double Exponential Moving Average
    dema = talib.DEMA(close, timeperiod=30)
    # Exponential Moving Average
    ema = talib.EMA(close, timeperiod=30)
    # Hilbert Transform - Instantaneous Trendline
    ht_trendline = talib.HT_TRENDLINE(close)
    # Kaufman Adaptive Moving Average
    kama = talib.KAMA(close, timeperiod=30)
    # Moving average
    ma = talib.MA(close, timeperiod=30, matype=0)
    # MESA Adaptive Moving Average
    mama = talib.MAMA(close, fastlimit=0, slowlimit=0)
    # Moving average with variable period
    mavp = talib.MAVP(close, periods, minperiod=2, maxperiod=30, matype=0)
    # MidPoint over period
    midpoint = talib.MIDPOINT(close, timeperiod=14)
    # Midpoint Price over period
    midprice = talib.MIDPRICE(high, low, timeperiod=14)
    # Parabolic SAR
    sar = talib.SAR(high, low, acceleration=0, maximum=0)
    # Parabolic SAR - Extended
    sarext = talib.SAREXT(high, low, startvalue=0, offsetonreverse=0, accelerationinitlong=0, accelerationlong=0, accelerationmaxlong=0, accelerationinitshort=0, accelerationshort=0, accelerationmaxshort=0)
    # Simple Moving Average
    sma = talib.SMA(close, timeperiod=30)
    # Triple Exponential Moving Average 
    t3 = talib.T3(close, timeperiod=5, vfactor=0)
    # Triple Exponential Moving Average
    tema = talib.TEMA(close, timeperiod=30)
    # Triangular Moving Average
    trima = talib.TRIMA(close, timeperiod=30)
    # Weighted Moving Average
    wma = talib.WMA(close, timeperiod=30)
    
    return bbands, dema, ema, ht_trendline, kama, ma, mama, mavp, midpoint, midprice, sar, sarext, sma, t3, tema, trima, wma

def statisticFunctions(open_, high, low, close, volume):
    # Beta
    beta = talib.BETA(high, low, timeperiod=5)
    # Pearson's Correlation Coefficient
    correl = talib.CORREL(high, low, timeperiod=30)
    # Linear Regression
    linearreg = talib.LINEARREG(close, timeperiod=14)
    # Linear Regression Angle
    linearreg_angle = talib.LINEARREG_ANGLE(close, timeperiod=14)
    # Linear Regression Intercept
    linearreg_intercept = talib.LINEARREG_INTERCEPT(close, timeperiod=14)
    # Linear Regression Slope
    linearreg_slope = talib.LINEARREG_SLOPE(close, timeperiod=14)
    # Standard Deviation
    stddev = talib.STDDEV(close, timeperiod=5, nbdev=1)
    # Time Series Forecast
    tsf = talib.TSF(close, timeperiod=14)
    # Variance
    var = talib.VAR(close, timeperiod=5, nbdev=1)
    
    return beta, correl, linearreg, linearreg_angle, linearreg_intercept, linearreg_slope, stddev, tsf, var

def momentumIndicator(open_, high, low, close, volume):
    # Average Directional Movement Index
    adx  = talib.ADX(high, low, close, timeperiod=14)
    # Average Directional Movement Index Rating
    adxr = talib.ADXR(high, low, close, timeperiod=14)
    # Absolute Price Oscillator
    apo = talib.APO(close, fastperiod=12, slowperiod=26, matype=0)
    # Aroon
    aroondown, aroonup = talib.AROON(high, low, timeperiod=14)
    #Aroon Oscillator
    arronosc = talib.AROONOSC(high, low, timeperiod=14)
    #Balance Of Power
    bop = talib.BOP(open_, high, low, close)
    #Commodity Channel Index
    cci = talib.CCI(high, low, close, timeperiod=14)
    #Chande Momentum Oscillator
    cmo = talib.CMO(close, timeperiod=14)
    # Directional Movement Index
    dx = talib.DX(high, low, close, timeperiod=14)
    # Moving Average Convergence/Divergence
    macd, macdsignal, macdhist = talib.MACD(close, fastperiod=12, slowperiod=26, signalperiod=9)
    # Money Flow Index
    mfi = talib.MFI(high, low, close, volume, timeperiod=14)
    # Minus Directional Indicator
    mdi = talib.MINUS_DI(high, low, close, timeperiod=14)
    # Minus Directional Movement
    mdm = talib.MINUS_DM(high, low, timeperiod=14)
    # Momentum
    mom = talib.MOM(close, timeperiod=10)
    # Plus Directional Indicator
    pdi = talib.PLUS_DI(high, low, close, timeperiod=14)
    # Plus Directional Movement
    pdm = talib.PLUS_DM(high, low, timeperiod=14)
    # Percentage Price Oscillator
    ppo = talib.PPO(close, fastperiod=12, slowperiod=26, matype=0)
    # Rate of change : ((price/prevPrice)-1)*100
    roc = talib.ROC(close, timeperiod=10)
    # Rate of change Percentage: (price-prevPrice)/prevPrice
    rocp = talib.ROCP(close, timeperiod=10)
    # ROCR - Rate of change ratio: (price/prevPrice)
    rocr = talib.ROCR(close, timeperiod=10)
    # Rate of change ratio 100 scale: (price/prevPrice)*100
    rocr1000 = talib.ROCR100(close, timeperiod=10)
    # Relative Strength Index
    rsi = talib.RSI(close, timeperiod=14)
    # Stochastic
    slowk, slowd = talib.STOCH(high, low, close, fastk_period=5, slowk_period=3, slowk_matype=0, slowd_period=3, slowd_matype=0)
    # Stochastic Fast
    fastk, fastd = talib.STOCHF(high, low, close, fastk_period=5, fastd_period=3, fastd_matype=0)
    # Stochastic Relative Strength Index
    fastkRSI, fastdRSI = talib.STOCHRSI(close, timeperiod=14, fastk_period=5, fastd_period=3, fastd_matype=0)
    # 1-day Rate-Of-Change (ROC) of a Triple Smooth EMA
    trix = talib.TRIX(close, timeperiod=30)
    #Ultimate Oscillator
    ultsoc = talib.ULTOSC(high, low, close, timeperiod1=7, timeperiod2=14, timeperiod3=28)
    #Williams' %R
    willr = talib.WILLR(high, low, close, timeperiod=14)
    
    return adx, adxr, apo, aroondown, aroonup, arronosc, bop, \
            cci, cmo, dx, macd, macdsignal, macdhist, mfi, mdi, \
            mdm, mom, pdi, pdm, ppo, roc, rocp, rocr, rocr1000, \
            rsi, slowk, slowd, fastk, fastd, fastkRSI, fastdRSI, \
            trix, ultsoc, willr

def volumeIndicators(open_, high, low, close, volume):
    # Chaikin A/D Line
    ad = talib.AD(high, low, close, volume)
    # Chaikin A/D Oscillator
    adosc = talib.ADOSC(high, low, close, volume, fastperiod=3, slowperiod=10)
    # On Balance Volume
    obv = talib.OBV(close, volume)
    return ad, adosc, obv

