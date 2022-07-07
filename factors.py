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

def cycleIndicators(open_, high, low, close, volume):
    # Hilbert Transform - Dominant Cycle Period
    ht_dcperiod = talib.HT_DCPERIOD(close)
    # Hilbert Transform - Dominant Cycle Phase
    ht_dcphase = talib.HT_DCPHASE(close)
    # Hilbert Transform - Phasor Components
    ht_phasor = talib.HT_PHASOR(close)
    # Hilbert Transform - SineWave
    ht_sine = talib.HT_SINE(close)
    # Hilbert Transform - Trend vs Cycle Mode
    ht_trendmode = talib.HT_TRENDMODE(close)
    
    return ht_dcperiod, ht_dcphase, ht_phasor, ht_sine, ht_trendmode

def priceTransform(open_, high, low, close, volume):
    # Average Price
    avgprice = talib.AVGPRICE(open_, high, low, close)
    # Median Price
    medprice = talib.MEDPRICE(high, low)
    # Typical Price
    typprice = talib.TYPPRICE(high, low, close)
    # Weighted Close Price
    wclprice = talib.WCLPRICE(high, low, close)
    
    return avgprice, medprice, typprice, wclprice

def volatilityIndicators(open_, high, low, close, volume):
    # Average True Range
    atr = talib.ATR(high, low, close, timeperiod=14)
    # Normalized Average True Range
    natr = talib.NATR(high, low, close, timeperiod=14)
    # True Range
    trange = talib.TRANGE(high, low, close)
    
    return atr, natr, trange

def patternRecognition(open_, high, low, close, volume):
    # Two Crows
    cdl2crows = talib.CDL2CROWS(open_, high, low, close)
    # Three Black Crows
    cdl3blackrows = talib.CDL3BLACKCROWS(open_, high, low, close)
    # Three Inside Up/Down
    cdl3inside = talib.CDL3INSIDE(open_, high, low, close)
    # Three-Line Strike
    cdl3linestrike = talib.CDL3LINESTRIKE(open_, high, low, close)
    # Three Outside Up/Down
    cdl3outside = talib.CDL3OUTSIDE(open_, high, low, close)
    # Three Stars In The South
    cdl3starsinsouth = talib.CDL3STARSINSOUTH(open_, high, low, close)
    # Three Advancing White Soldiers
    cdl3whitesoldiers = talib.CDL3WHITESOLDIERS(open_, high, low, close)
    # Abandoned Baby
    cdlabandonedbaby = talib.CDLABANDONEDBABY(open_, high, low, close, penetration=0)
    # Advance Block
    cdladvanceblock = talib.CDLADVANCEBLOCK(open_, high, low, close)
    # Belt-hold
    cdlbelthold = talib.CDLBELTHOLD(open_, high, low, close)
    # Breakaway
    cdlbreakaway = talib.CDLBREAKAWAY(open_, high, low, close)
    # Closing Marubozu
    cdlclosingmarubozu = talib.CDLCLOSINGMARUBOZU(open_, high, low, close)
    # Concealing Baby Swallow
    cdlconcealbabyswall = talib.CDLCONCEALBABYSWALL(open_, high, low, close)
    # Counterattack
    cdlcounterattack = talib.CDLCOUNTERATTACK(open_, high, low, close)
    # Dark Cloud Cover
    cdlddarkcloudcover = talib.CDLDARKCLOUDCOVER(open_, high, low, close, penetration=0)
    # Doji
    cdldoji = talib.CDLDOJI(open_, high, low, close)
    # Doji Star
    cdldojistar = talib.CDLDOJISTAR(open_, high, low, close)
    # Dragonfly Doji
    cdldragonflydoji = talib.CDLDRAGONFLYDOJI(open_, high, low, close)
    # Engulfing Pattern
    cdlengulfing = talib.CDLENGULFING(open_, high, low, close)
    # Evening Doji Star
    cdleveningdojistar = talib.CDLEVENINGDOJISTAR(open_, high, low, close, penetration=0)
    # Evening Star
    cdleveningstar = talib.CDLEVENINGSTAR(open_, high, low, close, penetration=0)
    # Up/Down-gap side-by-side white lines
    cdlgapsidewhite = talib.CDLGAPSIDESIDEWHITE(open_, high, low, close)
    # Gravestone Doji
    cdlgravestonedoji = talib.CDLGRAVESTONEDOJI(open_, high, low, close)
    # Hammer
    hammer = talib.CDLHAMMER(open_, high, low, close)
    # Hanging Man
    hangingman = talib.CDLHANGINGMAN(open_, high, low, close)
    # Harami Pattern
    cdlharami = talib.CDLHARAMI(open_, high, low, close)
    # Harami Cross Pattern
    cdlharamiicross = talib.CDLHARAMICROSS(open_, high, low, close)
    # High-Wave Candle
    cdlhighwave = talib.CDLHIGHWAVE(open_, high, low, close)
    # Hikkake Pattern
    cdlhikkake = talib.CDLHIKKAKE(open_, high, low, close)
    # Modified Hikkake Pattern
    cdlhikkakemod = talib.CDLHIKKAKEMOD(open_, high, low, close)
    # Homing Pigeon
    cdlhomiingpigeon = talib.CDLHOMINGPIGEON(open_, high, low, close)
    # Identical Three Crows
    cdlidentical3crows = talib.CDLIDENTICAL3CROWS(open_, high, low, close)
    # In-Neck Pattern
    cdlinneck = talib.CDLINNECK(open_, high, low, close)
    # Inverted Hammer
    cdlinvertedhammer = talib.CDLINVERTEDHAMMER(open_, high, low, close)
    # Kicking
    cdlkiicking = talib.CDLKICKING(open_, high, low, close)
    # Kicking - bull/bear determined by the longer marubozu
    cdlkickingbylength = talib.CDLKICKINGBYLENGTH(open_, high, low, close)
    # Ladder Bottom
    cdlladderbottom = talib.CDLLADDERBOTTOM(open_, high, low, close)
    # Long Legged Doji
    cdllongleggeddoji = talib.CDLLONGLEGGEDDOJI(open_, high, low, close)
    # Long Line Candle
    cdllongline = talib.CDLLONGLINE(open_, high, low, close)
    # Marubozu
    cdlmarubozu = talib.CDLMARUBOZU(open_, high, low, close)
    # Matching Low
    cdlmatchinglow = talib.CDLMATCHINGLOW(open_, high, low, close)
    # Mat Hold
    cdlmathold = talib.CDLMATHOLD(open_, high, low, close, penetration=0)
    # Morning Doji Star
    cdlmorningdojistar = talib.CDLMORNINGDOJISTAR(open_, high, low, close, penetration=0)
    # Morning Star
    cdlmorningstar = talib.CDLMORNINGSTAR(open_, high, low, close, penetration=0)
    # On-Neck Pattern
    cdlonneck = talib.CDLONNECK(open_, high, low, close)
    # Piercing Pattern
    cdlpiercing = talib.CDLPIERCING(open_, high, low, close)
    # Rickshaw Man
    cdlrickshawman = talib.CDLRICKSHAWMAN(open_, high, low, close)
    # Rising/Falling Three Methods
    cdlriesfall3methods = talib.CDLRISEFALL3METHODS(open_, high, low, close)
    # Separating Lines
    cdseparatinglines = talib.CDLSEPARATINGLINES(open_, high, low, close)
    # Shooting Star
    cdlshootingstar = talib.CDLSHOOTINGSTAR(open_, high, low, close)
    # Short Line Candle
    cdlshortline = talib.CDLSHORTLINE(open_, high, low, close)
    # Spinning Top
    cdlspinningtop = talib.CDLSPINNINGTOP(open_, high, low, close)
    # Stalled Pattern
    cdlstalledpatter = talib.CDLSTALLEDPATTERN(open_, high, low, close)
    # Stick Sandwich
    cdlsticksandwich = talib.CDLSTICKSANDWICH(open_, high, low, close)
    # Takuri (Dragonfly Doji with very long lower shadow)
    cdltakuri = talib.CDLTAKURI(open_, high, low, close)
    # Tasuki Gap
    cdltasukigap = talib.CDLTASUKIGAP(open_, high, low, close)
    # Thrusting Pattern
    cdlthrusting = talib.CDLTHRUSTING(open_, high, low, close)
    # Tristar Pattern
    cdltristar = talib.CDLTRISTAR(open_, high, low, close)
    # Unique 3 River
    cdlunique3river = talib.CDLUNIQUE3RIVER(open_, high, low, close)
    # Upside Gap Two Crows
    cdlupsidegap2crows = talib.CDLUPSIDEGAP2CROWS(open_, high, low, close)
    # Upside/Downside Gap Three Methods
    cdlxsidegap3methods = talib.CDLXSIDEGAP3METHODS(open_, high, low, close)
    
    return cdl2crows, cdl3blackrows, cdl3inside, cdl3linestrike, cdl3outside, cdl3starsinsouth,\
            cdl3whitesoldiers, cdlabandonedbaby, cdladvanceblock, cdlbelthold,  cdlbreakaway, \
            cdlclosingmarubozu, cdlconcealbabyswall, cdlcounterattack, cdlddarkcloudcover, \
            cdldoji, cdldojistar, cdldragonflydoji, hammer, hangingman, cdlharami, cdlharamiicross,\
            cdlhighwave, cdlhikkake, cdlhikkakemod, cdlhomiingpigeon, cdlidentical3crows,\
            cdlinneck, cdlinvertedhammer, cdlkiicking, cdlkickingbylength, cdlladderbottom, cdllongleggeddoji, \
            cdllongline, cdlmarubozu, cdlmatchinglow, cdlmathold, cdlmorningdojistar, cdlmorningstar, \
            cdlonneck, cdlpiercing, cdlrickshawman, cdlriesfall3methods, cdseparatinglines, \
            cdlshootingstar, cdlshortline, cdlspinningtop, cdlstalledpatter, cdlsticksandwich, \
            cdltakuri, cdltasukigap, cdlthrusting, cdltristar, cdlunique3river, cdlupsidegap2crows, \
            cdlxsidegap3methods 
