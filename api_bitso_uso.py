# -*- coding: utf-8 -*-
"""
Api de Bitso
https://github.com/bitsoex/bitso-py
@author: Alexis
"""
#Importar libreria, modulo
import bitso

#Crear instancia con nuestras credenciales
API_KEY=''
API_SECRET=''
api = bitso.Api(API_KEY,API_SECRET)
#Libros (paridades) disponibles para intercambio
books = api.available_books()
books.books
#btc_mxn
#major_minor
#major:criptomoneda
#minor:moneda fiat
#De el libro especifico da el monto minimo de inversion
books.btc_mxn.minimum_amount

##Informacion del precio
#Información publica del libro especifico
tick = api.ticker('btc_mxn')
tick
tick.created_at

#Ordenes publicas del libro
ob = api.order_book('btc_mxn')
ob
ob.updated_at

#Intercambios publicos
trades = api.trades('btc_mxn')
trades
trades[0].price
trades[0].amount

#fees (comisiones)
fees = api.fees()
fees.btc_mxn.fee_percent

#Mi información
#Account Status
status = api.account_status()
status

#balance
balances = api.balances()
balances

#User Trades (mis intercambios)
myut = api.user_trades()
myut
myut[0].book


#Poner una orden
## Places a buy limit order.
## [book] - Specifies which book to use (btc_mxn, eth_mxn)
##                    - str
## [side] - the order side (buy, sell) 
##                    - str
## [order_type] - the order type (limit, market) 
##                    - str
## amount - Amount of major currency to buy.
##        - string
## major  - The amount of major currency for this order. An order must be specified in terms of major or minor, never both.
##        - string. Major denotes the cryptocurrency, in our case Bitcoin (BTC) or Ether (ETH).
## minor  - The amount of minor currency for this order. Minor denotes fiat currencies, in our case Mexican Peso (MXN)
##        - string
## price  - Price per unit of major. For use only with limit orders
##        - string
balances.usd.total
order = api.place_order(book='usd_mxn', side='sell', order_type='limit', major='5', price='40.00')
order

#Open Orders (mis ordenes abiertas)
oo = api.open_orders('usd_mxn')
oo

#Cancel order (cancelar ordenes)
api.cancel_order(order['oid'])
#u'true' #on success
