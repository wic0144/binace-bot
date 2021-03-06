from flask import Flask , request

from binance_connect import SIGNALS_BY_SYMBOLS
import threading
from config_prod import *






app = Flask(__name__)



run = True

# def worker():
    
#     while run:
#         print(run)
#         print("=======SCANNOW=======")
#         job()
#         time.sleep(10)
#         print("=====================")

class SIGNALS_MORNITORING(threading.Thread):
    
    def __init__(self,coins_list = []):
        self.need_to_break = False
        self.coins_list = []
    
    def job(self):
        print("CHECKING FOR SIGNALS PLEASE WAITS")

        coin_list = ["SANDUSDT"]
        for coin in coin_list:
            print(coin)
            r = SIGNALS_BY_SYMBOLS(coin)
            if r == "BUY":
                print("BUY NOW")
            
            elif r == "SELL":
                print("SELL NOW")
            
            else:
                print("NO SIGNALS")
    
    def run(self):
        print(self.need_to_break)
        while True:
            if not self.need_to_break:
                print("=======SCANNOW=======")
                self.job()
                time.sleep(10)
                print("=====================")
            
            elif not self.need_to_break:
                print("BOT STOP NOW")
            
            else:
                print("BOT KILLED")
                break
    
    def stop(self):
        print("Stop Signals")
        self.need_to_break = True
    
    def resume(self,command):
        print("Resume Signals")
        self.need_to_break = command
    
    
    
    



SM = SIGNALS_MORNITORING()
SM_t = threading.Thread(target=SM.run,daemon=True)

@app.route("/<START>", methods=['GET'])
def stop_app(START):
    if START=="START":
        try:
            SM_t.start()
        except:
            SM.resume(command=False)
            SM.run()

    elif START=="STOP":
        SM.stop()

    return "ok"


@app.route("/", methods=['GET','POST'])
def test_signals():
    try:
      print(x)
    except:
      print('An exception occurred')
    if request.method == "GET":
        msg = request.data.encode("utf-8")

        """
        PYBOTT : EASY EMA: order
        {{strategy.order.action}}
        @ {{strategy.order.contracts}}
        filled on {{ticker}}.
        New strategy position is
        {{strategy.position_size}}
        """
        #????????????????????? BTCUSDT ?????????
        #if symbol , signals
            #PlaceSELL
        #else
            #PlaceBUY
        
        return "This is buying signals"

    else:
        return "????????????????????? Link ????????????????????????????????? Webhook Tradingview"

@app.route("/<pairname>")
def pair_signals(pairname):

    """
    binance , Talibs , matplotlib
    """
    return "This is {} buying signals".format(pairname)

if __name__ == '__main__':
    app.run()
