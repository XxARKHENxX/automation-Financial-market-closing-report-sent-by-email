listPares = [("^BVSP", "IBOVESPA"), 
             ("^GSPC", "S&P500"), 
             ("BRL=X", "DOLAR"), 
             ("ABEV3.SA", "AMBEV"), 
             ("PBR", "PETROBRAS")]

mapaTickers = dict(listPares)

def FindName(ticker: str):   
    return mapaTickers.get(ticker, None)