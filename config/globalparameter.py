# coding:utf-8
from pathlib import Path
from urllib.parse import urljoin

import yaml

from src.api.gofreight_config import GoFreightConfig
from src.api.me import Me

'''
配置全域參數
'''
# 獲取專案路徑（因為 windows 執行時需要絕對路徑才能執行通過）
project_path = Path.cwd()

slack_channel_path = project_path/'config/slack_channel.yml'
gsheet_client_secret_path = project_path/'config/client_secret.json'
gsheet_config_path = project_path/'config/gsheet_config.yml'

# ======================================
# Global variable for every shipment
# ======================================
tp_name = ['AIR9191', 'BANK9191', 'CUSTOMER9191', 'CUSBROKER9191', 'FORWARDER9191', 'OCEAN9191', 'OTHERS9191', 'OVERSEAS9191', 'RAIL9191', 'RAMP9191', 'SHIPPER9191', 'TERMINAL9191', 'TRUCKER9191', 'WAREHOUSE9191']
vessel_list = ['CMA CGM ALEXANDER VON HUMBOLDT', 'CSCL BOHAI SEA', 'BRITTONA', 'FM 5', 'CODLI']
bill_to_nick_name = {'LOHAN': 'LHL', 'SFI':'STRAIGHT FORWARDING, INC.', 'EWI': 'EASYWAY INTERNATIONAL LLC', 'OLC': '东方超捷国际货运代理(深圳)有限公司青岛分公司'}
city_list = ['NEW TAIPEI CITY', 'TAIPEI CITY', 'TAOHYAN CITY', 'HSINCHU CITY', 'TAICHUNG CITY', 'CHANGHUA COUNTY', 'KEELUNG CITY', 'LIENCHIANG COUNTY', 'YILAN COUNTY', 'Diaoyutai', 'MIAOLI COUNTY', 'NANTOU COUNTY', 'CHIAYI COUNTY', 'YULIN COUNTY', 'TAINAN CITY', 'KAOHSIUNG CITY', 'KIMEN COUNTY', 'PINGTUNG COUNTY', 'TAITUNG COUNTY', 'HUALIEN COUNTY']
port_list = ['USZZX', 'USZZH', 'USZZC', 'USZZB', 'USZYY', 'USZYX', 'USZYT', 'USZYN', 'USZYL', 'USZYK']
commodity_list = ['APPLE', 'ORANGE', 'WATERMELON', 'PLASTIC', 'TOYS', 'CAMERA', 'MOTOCYCLE', 'GIFT', 'COMPUTER', 'CHAIR', 'DESK', 'CANDY', 'NOTEBOOK', 'BOOKS', 'MOBILE', 'PHONE']
model_list = ['Volvo','BMW','Toyota','Honda','Mercedes','Opel', 'VW', 'Nissan']
color_list = ['Orange', 'Red', 'White', 'Green', 'Blue', 'Black', 'Yellow', 'Grey', 'Purple']
sales_list = ['sales'] #Todo replace by api
unit_list = ['AEROSOL', 'ARTICLES', 'AUTO', 'BAG', 'BAGS', 'BALES', 'BALL', 'BALLOON', 'BALLOTS', 'BAR', 'BARGE', 'BARREL', 'BARRELS', 'BASKETS', 'BEAM', 'BIB', 'BIN', 'BLOCKS', 'BOARD', 'BOBBIN', 'BOLT', 'BOTTLE', 'BOTTLERACK', 'BOX', 'BOXES', 'BRIQUETTES', 'BUCKET', 'BULK', 'BULK, LIQUEFIED GAS', 'BULK,GAS', 'BULK,LIQUID', 'BUNCH', 'BUNDLE', 'BUNDLES', 'CAGE', 'CANISTER', 'CANVAS', 'CAR', 'CARBOY', 'CARD', 'CARTON', 'CARTONS', 'CASE', 'CASES', 'CASK', 'CHEESES', 'CHEST', 'CHURN', 'COFFER', 'COFFIN', 'COIL', 'COLLAPSIBLE TUBE', 'COLLIE', 'CONES', 'CONTAINER', 'CORD', 'COVER', 'CRADLE', 'CRATE', 'CRATES', 'CREEL', 'CUBE', 'CUBITAINER', 'CUP', 'CYLINDER', 'DRUM', 'DRUMS', 'ENVELOPE', 'FILMPACK', 'FIRKIN', 'FLASK', 'FLEXITANK', 'FOOTLOCKER', 'FORWARD', 'FRAME', 'FRAMED CRATE', 'FRUIT CRATE', 'GALLON', 'GARMENTS ON HANGERS', 'GIRDER', 'GIRDERS', 'GLASS BOTTLE', 'GUNNY BAGS', 'GUNNY BALES', 'HAMPER', 'HANGER', 'HEADS OF BEEF', 'HOGSHEAD', 'IBC', 'INGOT', 'INGOTS', 'IRON CASES', 'ITEM', 'JAR', 'JUG', 'JUTEBAG', 'KEG', 'KIT', 'LIFT', 'LIFT VAN', 'LOG', 'LOOSE', 'LOT', 'LUGS', 'MASTER CARTON', 'MAT', 'MATCH BOX', 'MILK CRATE', 'MULTIPLE BAGS', 'MULTIWALL SACK', 'NEST', 'NET', 'NOIL', 'NUMBERS', 'ON OWN WHEELS', 'OVERWRAP', 'PACKAGE', 'PACKAGES', 'PACKAGES', 'PACKS', 'PAIL', 'PALLET', 'PALLETS', 'PAPER BAG', 'PARCEL', 'PIECES', 'PIMS', 'PIPE', 'PITCHER', 'PLANK', 'PLASTIC BAG', 'PLASTIC BOTTLE', 'PLASTIC CASK', 'PLASTIC PALLETS', 'PLATE', 'PLATFORM', 'PLYWOOD', 'PLYWOOD BOX', 'PLYWOOD BOXCARTON BOX', 'PLYWOOD BOXS', 'PLYWOOD CASE', 'PLYWOOD CASES', 'PLYWOOD PALLET', 'PLYWOOD PALLETS', 'POLYBAG', 'POT', 'POUCH', 'PROCESSED WOOD', 'QE', 'QUARTERS OF BEEF', 'RACK', 'RAIL', 'REDNET', 'REELS', 'RING', 'ROD', 'ROLL', 'ROLLS', 'SACHET', 'SACK', 'SEA-CHEST', 'SEAVAN', 'SET', 'SETS', 'SHALLOW CRATE', 'SHEET', 'SHEETMETAL', 'SHOOK', 'SHRINKWRAPPED', 'SIDES OF BEEF', 'SKID', 'SLABS', 'SLEEVE', 'SOWS', 'SPINDLE', 'SPOOL', 'SUITCASE', 'SUPERSACS', 'TANK', 'TANK, CYLINDRICAL', 'TEA-CHEST', 'TIERCE', 'TIN', 'TIRES', 'TOTE', 'TRAY PACK', 'TRUNK', 'TRUSS', 'TUB', 'TUBE', 'TUN', 'UNITS', 'UNPACKED', 'VACUUMPACKED', 'VAT', 'VENEER BOARD BOXES', 'VENEER CASE', 'VIAL', 'WHEELED CARRIER', 'WICKERBOTTLE', 'WOODEN BOX', 'WOODEN BUNDLE', 'WOODEN CASE', 'WOODEN CASES', 'WOODEN CRATES', 'WOODEN PALLETS', 'WOVEN BAGS']

# ==============================
# LB2KG & CBM2CFT rule
# ==============================
LB2KG = 0.45359237
KG2LB = 2.20462262
CFT2CBM = 0.02831685
CBM2CFT = 35.31466247
AMOUNT_DELTA = 0.011

# ==============================
# '0' = Headless mode
# '1' = Main window
# ==============================
monitor = '1'

# ==============================
# Select Office & URL
# 'SFI'
# 'LOHAN'
# 'OLC'
# 'MASCOT'
# ==============================
company = None

# ==============================
# 'DEBUG'
# 'INFO'
# 'WARNING'
# 'ERROR'
# ==============================
log_level = 'DEBUG'

# ==============================
# All Project Path
# ==============================
# shipment datas json file path
info_path = project_path/'info'
oi_info_file = info_path/'oi_info.json'
oe_info_file = info_path/'oe_info.json'
ai_info_file = info_path/'ai_info.json'
ae_info_file = info_path/'ae_info.json'
tk_info_file = info_path/'tk_info.json'
wh_receipt_ot_info_file = info_path/'receipt_ot_info.json'
wh_receipt_am_info_file = info_path/'receipt_am_info.json'

log_path = project_path/'log'
download_path = project_path/'download'
download_path_tk = download_path/'tk'
patch_db_msg_path = project_path/'config'/'patch_db_msg.yml'
test_set_path = project_path/'config'/'test_set.yml'
test_runtime_path = project_path/'config'/'test_runtime.yml'
features_path = project_path/'features'
report_path = project_path/'report'
console_output_path = project_path/'console_output'

def read_company_config_files():
    with open(project_path/'config/company_config.yml', encoding='UTF-8') as f:
        global companyConfig
        companyConfig = yaml.safe_load(f)

def init_url(custom_base_url = None):
    class URLObject:
        def __init__(self, base_url):
            self.DASHBOARD = base_url
            self.LOGIN = urljoin(base_url, '/login/')
            self.LOGOUT = urljoin(base_url, '/logout/')
            self.PROFILE = urljoin(base_url, '/profile/')
            self.OI_NEW_SHIPMENT = urljoin(base_url, '/ocean/import/shipment/')
            self.OE_NEW_SHIPMENT = urljoin(base_url, '/ocean/export/shipment/')
            self.OE_NEW_BOOKING = urljoin(base_url, '/ocean/export/booking/entry/')
            self.OE_BOOKING_LIST = urljoin(base_url, '/ocean/export/booking/list/')
            self.OE_NEW_VESSEL_SCHEDULE = urljoin(base_url, '/ocean/export/vessel-schedule/entry/')
            self.AI_NEW_SHIPMENT = urljoin(base_url, '/air/import/shipment/')
            self.AE_NEW_SHIPMENT = urljoin(base_url, '/air/export/shipment/')
            self.AE_MAWB_STOCK_LIST = urljoin(base_url, '/air/mawb-no-stock/list/')
            self.TK_NEW_SHIPMENT = urljoin(base_url, '/truck/shipment/')
            self.MS_NEW_OPERATION = urljoin(base_url, '/misc/shipment/')
            self.WH_NEW_RECEIPTS = urljoin(base_url, '/warehouse/receipt/entry/')
            self.WH_NEW_RECEIVING = urljoin(base_url, '/warehouse/receiving/entry/')
            self.WH_NEW_SHIPPING = urljoin(base_url, '/warehouse/shipping/entry/')

            self.NEW_QUOTATION = urljoin(base_url, '/sales/quotation/entry/')
            self.NEW_TRADE_PARTNER = urljoin(base_url, '/sales/trade-partner/')
            self.TRADE_PARTNER_LIST = urljoin(base_url, '/sales/trade-partner/list/')
            self.CREATE_USER = urljoin(base_url, '/settings/user/management/create/')
            self.TRACKING_USER_MANAGEMENT = urljoin(base_url, '/settings/tracking-user/management/')
            self.CREATE_TRACKING_USER = urljoin(base_url, '/settings/tracking-user/management/profile/')
            self.FEATURE_AND_APROVAL = urljoin(base_url, '/settings/approval/rules/')
            self.PERMISSION_MANAGEMENT = urljoin(base_url, '/superuser/permission/management/')
            self.OFFICE_MANAGEMENT = urljoin(base_url, '/superuser/office/management/')
            self.COMPANY_MANAGEMENT = urljoin(base_url, '/superuser/company/entry/')
            self.SYSTEM_CONFIGURATION = urljoin(base_url, '/superuser/system-config/entry/')
            self.RESET_BACKUPS_DB = urljoin(base_url, '/superuser/super/reset-backups-db/')
            self.AWB_NO_MANAGEMENT = urljoin(base_url, '/settings/awb-no-range/')
            self.PATCH_DB = urljoin(base_url, '/superuser/super/patch-db/')

            self.VOLUME_AND_PROFIT_CHART = urljoin(base_url, '/mgmt/vp-chart/')
            self.VOLUME_AND_PROFIT_REPORT = urljoin(base_url, '/mgmt/vp-report/')
            self.PAYMENT_PLAN_LIST = urljoin(base_url, '/accounting/payment-plan/list/')
            self.RECEIVE_PAYMENT = urljoin(base_url, '/accounting/payment/customer-payment/entry/')
            self.TRIAL_BALANCE = urljoin(base_url, '/accounting/report/trial-balance/')
            self.BALANCE_SHEET = urljoin(base_url, '/accounting/report/balance-sheet/')
            self.GENERAL_LEDGER_REPORT = urljoin(base_url, '/accounting/report/gl-report/')
            self.AGENT_LOCAL_STATEMENT = urljoin(base_url, '/accounting/report/agent-local-statement/')
            self.AGING_REPORT = urljoin(base_url, '/accounting/report/aging-report/')
            self.INCOME_STATEMENT = urljoin(base_url, '/accounting/report/income-statement/')
            self.JOURNAL_REPORT = urljoin(base_url, '/accounting/report/journal-report/')
            self.FRONT_DESK_PORTAL = urljoin(base_url, '/accounting/front-desk/list/')
            self.UNIFORM_INVOICE_MANAGEMENT = urljoin(base_url, '/accounting/front-desk/uni-invoice/management/')
            self.UNIFORM_INVOICE_SETTING = urljoin(base_url, '/accounting/front-desk/uni-invoice/setting/')

        def to_url(self, page_name:str) -> str:
            url_map = {
                'Dashboard': self.DASHBOARD,
                'Login': self.LOGIN,
                'Profile': self.PROFILE,
                'Ocean Import New Shipment': self.OI_NEW_SHIPMENT,
                'Ocean Export New Shipment': self.OE_NEW_SHIPMENT,
                'Air Import New Shipment': self.AI_NEW_SHIPMENT,
                'Air Export New Shipment': self.AE_NEW_SHIPMENT,
                'Air Import MAWB List': self.AE_MAWB_STOCK_LIST,
                'Truck New Shipment': self.TK_NEW_SHIPMENT,
                'Misc New Operation': self.MS_NEW_OPERATION,
                'New Receipt': self.WH_NEW_RECEIPTS,
                'New Receiving': self.WH_NEW_RECEIVING,
                'New Shipping': self.WH_NEW_SHIPPING,
                'New Quotation': self.NEW_QUOTATION,
                'New Trade Partner': self.NEW_TRADE_PARTNER,
                'Trade Partner List': self.TRADE_PARTNER_LIST,
                'Create User': self.CREATE_USER,
                'Permission Management': self.PERMISSION_MANAGEMENT,
                'Office Management': self.OFFICE_MANAGEMENT,
                'Company Management': self.COMPANY_MANAGEMENT,
                'System Configuration': self.SYSTEM_CONFIGURATION,
                'Reset Backups DB': self.RESET_BACKUPS_DB,
                'Payment Plan List': self.PAYMENT_PLAN_LIST,
                'Receive Payment':self.RECEIVE_PAYMENT,
                'Balance Sheet': self.BALANCE_SHEET,
                'Trial Balance': self.TRIAL_BALANCE,
                'General Ledger Report': self.GENERAL_LEDGER_REPORT,
                'Income Statement': self.INCOME_STATEMENT,
                'AWB No. Management': self.AWB_NO_MANAGEMENT,
                'Patch DB': self.PATCH_DB,
                'MAWB Stock List': self.AE_MAWB_STOCK_LIST,
                'Feature and Approval': self.FEATURE_AND_APROVAL,
                'Tracking User Management': self.TRACKING_USER_MANAGEMENT,
                'Create Tracking User': self.CREATE_TRACKING_USER,
            }

            return url_map[page_name]


    global URL; URL = URLObject(base_url=companyConfig[company]['url'] if custom_base_url == None else custom_base_url)

def init_gofreight_config():
    global gofreight_config; gofreight_config = GoFreightConfig(URL.DASHBOARD, companyConfig[company]['sa'], companyConfig[company]['sa_password'])

# login user 後，將user info 存到 globalparameter
def init_user_info(username: str, password: str):
    global user_info; user_info = Me(URL.DASHBOARD, username, password)
