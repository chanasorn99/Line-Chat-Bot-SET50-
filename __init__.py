from flask import Flask, request, abort
import requests
import json
from Project.Config import *
from uncleengineer import thaistock
app = Flask(__name__)


def GET_BTC_PRICE():
    data = requests.get('https://bx.in.th/api/')
    BTC_PRICE = data.text.split('BTC')[1].split('last_price":')[1].split(',"volume_24hours')[0]
    return BTC_PRICE
def Text():
     return Text

@app.route('/webhook', methods=['POST','GET'])
def webhook():
    if request.method == 'POST':
        payload = request.json

        Reply_token = payload['events'][0]['replyToken']
        print(Reply_token)
        message = payload['events'][0]['message']['text']
        print(message)

        if 'ราคาITD' in message :
            ITD = thaistock('ITD')
            Reply_messasge = 'ราคาหุ้น อิตาเลียนไทย ขณะนี้ : {}'.format(ITD)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif 'ราคาADVANC' in message :
            ADVANC = thaistock('ADVANC')
            Reply_messasge = 'ราคาหุ้น บริษัท แอดวานซ์ อินโฟร์ เซอร์วิส จำกัด (มหาชน) ขณะนี้ : {}'.format(ADVANC)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif 'ราคาAOT' in message :
            AOT = thaistock('AOT')
            Reply_messasge = 'ราคาหุ้น บริษัท ท่าอากาศยานไทย จำกัด (มหาชน) ขณะนี้ : {}'.format(AOT)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif 'ราคาAWC' in message :
            AWC = thaistock('AWC')
            Reply_messasge = 'ราคาหุ้น บริษัท แอสเสท เวิรด์ คอร์ป จำกัด (มหาชน) ขณะนี้ : {}'.format(AWC)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif 'ราคาBANPU' in message :
            BANPU = thaistock('BANPU')
            Reply_messasge = 'ราคาหุ้น บริษัท บ้านปู จำกัด (มหาชน) ขณะนี้ : {}'.format(BANPU)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif 'ราคาBBL' in message :
            BBL = thaistock('BBL')
            Reply_messasge = 'ราคาหุ้น ธนาคารกรุงเทพ จำกัด (มหาชน) ขณะนี้ : {}'.format(BBL)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif 'ราคาBDMS' in message :
            BDMS = thaistock('BDMS')
            Reply_messasge = 'ราคาหุ้น บริษัท กรุงเทพดุสิตเวชการ จำกัด(มหาชน) ขณะนี้ : {}'.format(BDMS)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif 'ราคาBEM' in message :
            BEM	 = thaistock('BEM')
            Reply_messasge = 'ราคาหุ้น บริษัท ทางด่วนและรถไฟฟ้ากรุงเทพ จำกัด (มหาชน) ขณะนี้ : {}'.format(BEM)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif 'ราคาBGRIM' in message :
            BGRIM = thaistock('BGRIM')
            Reply_messasge = 'ราคาหุ้น บริษัท บี.กริม เพาเวอร์ จำกัด (มหาชน) ขณะนี้ : {}'.format(BGRIM)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif 'ราคาBH' in message :
            BH = thaistock('BH')
            Reply_messasge = 'ราคาหุ้น บริษัท ทางด่วนและรถไฟฟ้ากรุงเทพ จำกัด (มหาชน) ขณะนี้ : {}'.format(BH)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif 'ราคาBJC' in message :
            BJC	 = thaistock('BJC')
            Reply_messasge = 'ราคาหุ้น บริษัท เบอร์ลี่ ยุคเกอร์ จำกัด (มหาชน) ขณะนี้ : {}'.format(BJC)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif 'ราคาBPP' in message :
            BPP = thaistock('BPP')
            Reply_messasge = 'ราคาหุ้น บริษัท บ้านปู เพาเวอร์ จำกัด (มหาชน) ขณะนี้ : {}'.format(BPP)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif 'ราคาBTS' in message :
            BTS	= thaistock('BTS')
            Reply_messasge = 'ราคาหุ้น บริษัท บีทีเอส กรุ๊ป โฮลดิ้งส์ จำกัด (มหาชน) (มหาชน) ขณะนี้ : {}'.format(BTS)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif 'ราคาCBG' in message :
            CBG = thaistock('CBG')
            Reply_messasge = 'ราคาหุ้น บริษัท คาราบาวกรุ๊ป จำกัด (มหาชน) ขณะนี้ : {}'.format(CBG)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif 'ราคาCPALL' in message :
            CPALL = thaistock('CPALL')
            Reply_messasge = 'ราคาหุ้น บริษัท ซีพี ออลล์ จำกัด (มหาชน) ขณะนี้ : {}'.format(CPALL)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif 'ราคาCPF' in message :
            CPF = thaistock('CPF')
            Reply_messasge = 'ราคาหุ้น บริษัท เจริญโภคภัณฑ์อาหาร จำกัด (มหาชน) ขณะนี้ : {}'.format(CPF)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif 'ราคาCPN' in message :
            CPN	 = thaistock('CPN')
            Reply_messasge = 'ราคาหุ้น บริษัท เซ็นทรัลพัฒนา จำกัด (มหาชน) ขณะนี้ : {}'.format(CPN)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif 'ราคาDELTA' in message :
            DELTA = thaistock('DELTA')
            Reply_messasge = 'ราคาหุ้น บริษัทเดลต้า อีเลคโทรนิคส์ (ประเทศไทย) จำกัด (มหาชน) ขณะนี้ : {}'.format(DELTA)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif 'ราคาDTAC' in message :
            DTAC = thaistock('DTAC')
            Reply_messasge = 'ราคาหุ้น บริษัท โทเทิ่ล แอ็คเซ็ส คอมมูนิเคชั่น จำกัด (มหาชน) ขณะนี้ : {}'.format(DTAC)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif 'ราคาEA' in message :
            EA = thaistock('EA')
            Reply_messasge = 'ราคาหุ้น บริษัท พลังงานบริสุทธิ์ จำกัด (มหาชน) ขณะนี้ : {}'.format(EA)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif 'ราคาEGCO' in message :
            EGCO = thaistock('EGCO')
            Reply_messasge = 'ราคาหุ้น บริษัท ผลิตไฟฟ้า จำกัด (มหาชน) ขณะนี้ : {}'.format(EGCO)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif 'ราคาGLOBAL	' in message :
            GLOBAL = thaistock('GLOBAL')
            Reply_messasge = 'ราคาหุ้น บริษัท สยามโกลบอลเฮ้าส์ จำกัด (มหาชน) ขณะนี้ : {}'.format(GLOBAL)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif 'ราคาGPSC' in message :
            GPSC = thaistock('GPSC')
            Reply_messasge = 'ราคาหุ้น บริษัท โกลบอล เพาเวอร์ ซินเนอร์ยี่ จำกัด (มหาชน) ขณะนี้ : {}'.format(GPSC)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif 'ราคาGULF' in message :
            GULF = thaistock('GULF')
            Reply_messasge = 'ราคาหุ้น บริษัท กัลฟ์ เอ็นเนอร์จี ดีเวลลอปเมนท์ จำกัด (มหาชน) ขณะนี้ : {}'.format(GULF)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif 'ราคาHMPRO' in message :
            HMPRO = thaistock('HMPRO')
            Reply_messasge = 'ราคาหุ้น บริษัท โฮม โปรดักส์ เซ็นเตอร์ จำกัด (มหาชน) ขณะนี้ : {}'.format(HMPRO)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif 'ราคาINTUCH	' in message :
            INTUCH	 = thaistock('INTUCH	')
            Reply_messasge = 'ราคาหุ้น บริษัท อินทัช โฮลดิ้งส์ จำกัด (มหาชน) ขณะนี้ : {}'.format(INTUCH)        
        elif 'ราคาIRPC' in message :
            IRPC = thaistock('IRPC')
            Reply_messasge = 'ราคาหุ้น บริษัท ไออาร์พีซี จำกัด (มหาชน) ขณะนี้ : {}'.format(IRPC)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif 'ราคาIVL' in message :
            IVL = thaistock('EGCO')
            Reply_messasge = 'ราคาหุ้น บริษัท อินโดรามา เวนเจอร์ส จำกัด (มหาชน) ขณะนี้ : {}'.format(IVL)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif 'ราคาKBANK	O' in message :
            KBANK	 = thaistock('KBANK	')
            Reply_messasge = 'ราคาหุ้น ธนาคารกสิกรไทย จำกัด (มหาชน) ขณะนี้ : {}'.format(KBANK	)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif 'ราคาKTB' in message :
            KTB = thaistock('KTB')
            Reply_messasge = 'ราคาหุ้น ธนาคารกรุงไทย จำกัด (มหาชน) ขณะนี้ : {}'.format(KTB)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif 'ราคาKTC' in message :
            KTC = thaistock('KTC')
            Reply_messasge = 'ราคาหุ้น บริษัท บัตรกรุงไทย จำกัด (มหาชน) ขณะนี้ : {}'.format(KTC)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif 'ราคาLH' in message :
            LH = thaistock('LH')
            Reply_messasge = 'ราคาหุ้น บริษัทแลนด์แอนด์เฮ้าส์ จำกัด (มหาชน) ขณะนี้ : {}'.format(LH)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif 'ราคาMINT' in message :
            MINT = thaistock('MINT')
            Reply_messasge = 'ราคาหุ้น บริษัท ไมเนอร์ อินเตอร์เนชั่นแนล จำกัด (มหาชน) ขณะนี้ : {}'.format(MINT)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif 'ราคาMTC' in message :
            MTC = thaistock('MTC')
            Reply_messasge = 'ราคาหุ้น บริษัท เมืองไทย แคปปิตอล จำกัด (มหาชน) ขณะนี้ : {}'.format(MTC)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif 'ราคาOSP' in message :
            OSP = thaistock('OSP')
            Reply_messasge = 'ราคาหุ้น บริษัท โอสถสภา จำกัด (มหาชน) ขณะนี้ : {}'.format(OSP)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif 'ราคาPTT' in message :
            PTT = thaistock('PTT')
            Reply_messasge = 'ราคาหุ้น บริษัท ปตท. จำกัด (มหาชน) ขณะนี้ : {}'.format(PTT)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif 'ราคาPTTEP' in message :
            PTTEP = thaistock('PTTEP')
            Reply_messasge = 'ราคาหุ้น บริษัท ปตท. สำรวจและผลิตปิโตรเลียม จำกัด (มหาชน) ขณะนี้ : {}'.format(PTTEP)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif 'ราคาPTTGC	' in message :
            PTTGC = thaistock('PTTGC	')
            Reply_messasge = 'ราคาหุ้น บริษัท พีทีที โกลบอล เคมิคอล จำกัด (มหาชน) ขณะนี้ : {}'.format(PTTGC)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif 'ราคาRATCH' in message :
            RATCH = thaistock('RATCH')
            Reply_messasge = 'ราคาหุ้น บริษัท ราช กรุ๊ป จำกัด (มหาชน) ขณะนี้ : {}'.format(RATCH)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif 'ราคาROBINS	' in message :
            ROBINS = thaistock('ROBINS')
            Reply_messasge = 'ราคาหุ้น บริษัท โรบินสัน จำกัด (มหาชน) ขณะนี้ : {}'.format(ROBINS)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif 'ราคาSAWAD' in message :
            SAWAD = thaistock('SAWAD')
            Reply_messasge = 'ราคาหุ้น บริษัท ศรีสวัสดิ์ คอร์ปอเรชั่น จำกัด (มหาชน) ขณะนี้ : {}'.format(SAWAD)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif 'ราคาSCB' in message :
            SCB = thaistock('SCB')
            Reply_messasge = 'ราคาหุ้น ธนาคารไทยพาณิชย์ จำกัด (มหาชน) ขณะนี้ : {}'.format(SCB)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif 'ราคาSCC' in message :
            SCC = thaistock('SCC')
            Reply_messasge = 'ราคาหุ้น  บริษัท ปูนซิเมนต์ไทย จำกัด(มหาชน) ขณะนี้ : {}'.format(SCC)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif 'ราคาTCAP' in message :
            TCAP = thaistock('TCAP')
            Reply_messasge = 'ราคาหุ้น บริษัท ทุนธนชาต จำกัด (มหาชน) ขณะนี้ : {}'.format(TCAP)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif 'ราคาTISCO' in message :
            TISCO = thaistock('TISCO')
            Reply_messasge = 'ราคาหุ้น บริษัท ทิสโก้ไฟแนนเชียลกรุ๊ป จำกัด (มหาชน) ขณะนี้ : {}'.format(TISCO)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif 'ราคาTMB' in message :
            TMB = thaistock('TMB')
            Reply_messasge = 'ราคาหุ้น ธนาคารทหารไทย จำกัด (มหาชน) ขณะนี้ : {}'.format(TMB)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif 'ราคาTOA' in message :
            TOA = thaistock('TOA')
            Reply_messasge = 'ราคาหุ้น บริษัท ทีโอเอ เพ้นท์ (ประเทศไทย) จำกัด (มหาชน) ขณะนี้ : {}'.format(TOA)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif 'ราคาTOP' in message :
            TOP = thaistock('TOP')
            Reply_messasge = 'ราคาหุ้น บริษัท ไทยออยล์ จำกัด (มหาชน) ขณะนี้ : {}'.format(TOP)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif 'ราคาTRUE' in message :
            TRUE = thaistock('TRUE')
            Reply_messasge = 'ราคาหุ้น บริษัท ทรู คอร์ปอเรชั่น จำกัด (มหาชน) ขณะนี้ : {}'.format(TRUE)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif 'ราคาTU' in message :
            TU = thaistock('TU')
            Reply_messasge = 'ราคาหุ้น บริษัท ไทยยูเนี่ยน กรุ๊ป จำกัด (มหาชน) ขณะนี้ : {}'.format(TU)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif 'ราคาWHA' in message :
            WHA = thaistock('WHA')
            Reply_messasge = 'ราคาหุ้น บริษัท ดับบลิวเอชเอ คอร์ปอเรชั่น จำกัด (มหาชน) (มหาชน) ขณะนี้ : {}'.format(WHA)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)


         ## Cryptocurrency ##
        elif "BTC" in message :
            Reply_messasge = 'ราคา BITCOIN ขณะนี้ : {}'.format(GET_BTC_PRICE())
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        ## set account ##
        elif "เปิดบัญชีหุ้น" in message :
            Reply_messasge = 'ในการเทรดหุ้น หรือซื้อขายหุ้นนั้น เราต้องเปิดบัญชีหุ้นกับโบรกเกอร์ หรือที่เรียกกันว่าเปิดพอร์ตนั่นเอง โบรกเกอร์ คือ บริษัทหลักทรัพย์ที่ทำหน้าที่รับคำสั่งซื้อขายหุ้นจากผู้ลงทุน แล้วส่งไปเข้าระบบซื้อขายของตลาดหลักทรัพย์เพื่อให้จับคู่คำสั่งซื้อขายโดยอัตโนมัติ ชำระเงินค่าซื้อหุ้น และนำหุ้นเข้าบัญชีของผู้ลงทุน  '.format(Text)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "บัญชีเงินสด" in message :
            Reply_messasge = 'บัญชีเงินสด เพียงวางเงินหลักประกันของมูลค่าที่ต้องการจะลงทุนทำให้ไม่จำเป็นต้องนำเงินลงทุนทั้งหมดที่มีอยู่ไปฝากไว้กับโบรกเกอร์โบรกเกอร์จะกำหนดวงเงินซื้อขายให้ โดยพิจารณาจากความสามารถในการชำระเงิน และฐานะทางการเงิน โดยจะซื้อขายได้ไม่เกินวงเงินที่กำหนดชำระเงินค่าซื้อหุ้นโดยตัดบัญชีธนาคาร 2 วันทำการ หลังจากวันซื้อหลักทรัพย์ (ระบบ ATS - Automatic Transfer System) '.format(Text)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "บัญชีหุ้น" in message :
            Reply_messasge = 'บัญชีหุ้นมี 3 ประเภทได้แก่ 1. บัญชีเงินสด 2. บัญชีแคชบาลานซ์ 3. บัญชีเครดิตบาลานซ์ '.format(Text)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "บัญชีแคชบาลานซ์" in message :
            Reply_messasge = 'บัญชีวางเงินล่วงหน้า/บัญชีเครดิตบาลานซ์ ช่วยป้องกันการซื้อหุ้นมากเกินความสามารถในการชำระเงิน โดยลูกค้านำเงินสดมาค้ำประกันไว้กับโบรกเกอร์ 100% ก่อนการลงทุนเงินค้ำประกันที่ฝากไว้กับโบรกเกอร์จะได้รับดอกเบี้ยจากบริษัทฯ ด้วย '.format(Text)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "หุ้นบุริมสิทธิ์" in message :
            Reply_messasge = 'เป็นตราสารที่ผู้ถือมีส่วนร่วมเป็นเจ้าของกิจการเช่นเดียวกับหุ้นสามัญ แม้จะไม่มีสิทธิในการออกเสียงลงมติในที่ประชุมผู้ถือหุ้น แต่เมื่อกิจการมีกำไรจากการดำเนินงาน ผู้ถือหุ้นบุริมสิทธิจะได้รับเงินปันผลในอัตราคงที่ ซึ่งอาจจะมากหรือน้อยกว่าผู้ถือหุ้นสามัญก็ได้ ขณะเดียวกัน หากกิจการนั้นต้องเลิกกิจการ และมีการชำระบัญชีโดยการขายทรัพย์สิน ผู้ถือหุ้นบุริมสิทธิ์ก็จะได้รับเงินคืนทุนก่อนผู้ถือหุ้นสามัญ '.format(Text)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        
        ## Broker ##
        elif "โบรกเกอร์คืออะไร" in message :
            Reply_messasge = 'นายหน้าซื้อขายหลักทรัพย์ ตัวแทนผู้ทำหน้าที่ซื้อหรือขายหุ้นในตลาดหลักทรัพย์ให้แก่ผู้ลงทุน โดยได้รับค่าธรรมเนียมหรือค่านายหน้าจากผู้ลงทุนเป็นผลตอบแทน'.format(Text)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "โบรกเกอร์" in message :
            Reply_messasge = 'รายชื่อโบรกเกอร์ 5 อันดับที่เป็นที่นิยมในขณะนี้\n1: Exness \n2: XM \n3: FXPrimus \n4: FXPRO \n5: pepperstone'.format(Text)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "ชื่อโบรกเกอร์" in message :
            Reply_messasge = 'รายชื่อโบรกเกอร์ 5 อันดับที่เป็นที่นิยมในขณะนี้\n1: Exness \n2: XM \n3: FXPrimus \n4: FXPRO \n5: pepperstone'.format(Text)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        

        ## check set
        elif "ราคาหุ้น" in message :
            Reply_messasge = 'ตรวจสอบหุ้น set50 ได้ที่ลิงค์นี้ \n https://marketdata.set.or.th/mkt/sectorquotation.do?sector=SET50&language=th&country=TH '.format(Text)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "Set50" in message :
            Reply_messasge = 'ตรวจสอบหุ้น set50 ได้ที่ลิงค์นี้ \n https://marketdata.set.or.th/mkt/sectorquotation.do?sector=SET50&language=th&country=TH '.format(Text)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "เล่น" in message :
            Reply_messasge = 'ต้องเปิดบัญชีซื้อขายหุ้นกับบริษัทหลักทรัพย์ หรือที่เรียกว่า “โบรกเกอร์” ก่อน และยังมี Application ที่ใช้สำหรับซื้อขายหุ้นที่คนส่วนใหญ่เล่นชื่อว่า Streaming'.format(Text)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "หุ้นน่าลงทุน" in message :
            Reply_messasge = 'ตรวจสอบหุ้น set50 ได้ที่ลิงค์นี้ \n https://marketdata.set.or.th/mkt/sectorquotation.do?sector=SET50&language=th&country=TH\nการลงทุนมีความเสี่ยง ผู้ลงทุนควรศึกษาข้อมูลก่อนการตัดสินใจลงทุน '.format(Text)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "หุ้น" in message :
            Reply_messasge = 'ตรวจสอบหุ้น set50 ได้ที่ลิงค์นี้ \n https://marketdata.set.or.th/mkt/sectorquotation.do?sector=SET50&language=th&country=TH \nการลงทุนมีความเสี่ยง ผู้ลงทุนควรศึกษาข้อมูลก่อนการตัดสินใจลงทุน'.format(Text)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "ซื้อ" in message :
            Reply_messasge = 'ตรวจสอบหุ้น set50 ได้ที่ลิงค์นี้ \n https://marketdata.set.or.th/mkt/sectorquotation.do?sector=SET50&language=th&country=TH \nการลงทุนมีความเสี่ยง ผู้ลงทุนควรศึกษาข้อมูลก่อนการตัดสินใจลงทุน'.format(Text)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        
        
        ## income ##
        elif "ส่วนต่างราคา" in message :
            Reply_messasge = 'กำไรจากส่วนต่างราคา โดยกำไรจาก Capital Gain จะเกิดจากการที่ขายสินทรัพย์แล้วได้กำไรจากส่วนต่างราคา อย่างเช่น การขายหุ้น ขายคอนโด ขายที่ดิน ขายหน่วยลงทุนของกองทุนรวม '.format(Text)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        
        ## how to play set ##
        elif "ลงทุน" in message :
            Reply_messasge = 'ต้องเปิดบัญชีซื้อขายหุ้นกับบริษัทหลักทรัพย์ หรือที่เรียกว่า “โบรกเกอร์” ก่อน และยังมี Application ที่ใช้สำหรับซื้อขายหุ้นที่คนส่วนใหญ่เล่นชื่อว่า Streaming'.format(Text)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "การเล่น" in message :
            Reply_messasge = 'ต้องเปิดบัญชีซื้อขายหุ้นกับบริษัทหลักทรัพย์ หรือที่เรียกว่า “โบรกเกอร์” ก่อน และยังมี Application ที่ใช้สำหรับซื้อขายหุ้นที่คนส่วนใหญ่เล่นชื่อว่า Streaming'.format(Text)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "วิธีซ้อหุ้น" in message :
            Reply_messasge = 'ต้องเปิดบัญชีซื้อขายหุ้นกับบริษัทหลักทรัพย์ หรือที่เรียกว่า “โบรกเกอร์” ก่อน และยังมี Application ที่ใช้สำหรับซื้อขายหุ้นที่คนส่วนใหญ่เล่นชื่อว่า Streaming'.format(Text)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "วิธีซ้อหุ้น" in message :
            Reply_messasge = 'ต้องเปิดบัญชีซื้อขายหุ้นกับบริษัทหลักทรัพย์ หรือที่เรียกว่า “โบรกเกอร์” ก่อน และยังมี Application ที่ใช้สำหรับซื้อขายหุ้นที่คนส่วนใหญ่เล่นชื่อว่า Streaming'.format(Text)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "เปิดพอร์ต" in message :
            Reply_messasge = 'ต้องเปิดบัญชีซื้อขายหุ้นกับบริษัทหลักทรัพย์ หรือที่เรียกว่า “โบรกเกอร์” ก่อน และยังมี Application ที่ใช้สำหรับซื้อขายหุ้นที่คนส่วนใหญ่เล่นชื่อว่า Streaming'.format(Text)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        


        ## greeting ##
        elif "สวัสดี" in message :
            Reply_messasge = 'สวัสดีครับผมคือบอทให้ความรู้เรื่องหุ้นครับ ^^ '.format(Text)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "ดี" in message :
            Reply_messasge = 'สวัสดีครับผมคือบอทให้ความรู้เรื่องหุ้นครับ ^^ '.format(Text)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "เห้" in message :
            Reply_messasge = 'สวัสดีครับผมคือบอทให้ความรู้เรื่องหุ้นครับ ^^ '.format(Text)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)    
        elif "Hi" in message :
            Reply_messasge = 'สวัสดีครับผมคือบอทให้ความรู้เรื่องหุ้นครับ ^^ '.format(Text)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "hi" in message :
            Reply_messasge = 'สวัสดีครับผมคือบอทให้ความรู้เรื่องหุ้นครับ ^^ '.format(Text)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "ชื่ออะไร" in message :
            Reply_messasge = 'สวัสดีครับผมคือบอทให้ความรู้เรื่องหุ้นครับ ^^ '.format(Text)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "ชื่อไร" in message :
            Reply_messasge = 'สวัสดีครับผมคือบอทให้ความรู้เรื่องหุ้นครับ ^^ '.format(Text)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "ทำไรได้" in message :
            Reply_messasge = 'สวัสดีครับผมคือบอทสามารถให้ความรู้เรื่องหุ้นและให้ข้อมูลเพื่อวิเคราะห์เปรียบเทียบหุ้นได้ครับบบ ^^ '.format(Text)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "ทำไร" in message :
            Reply_messasge = 'รอคุยกับคุณอยู่ไงง ^^ '.format(Text)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "เป็นไงบ้าง" in message :
            Reply_messasge = 'สบายดีครับบบบ ^^ '.format(Text)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "อ่อ" in message :
            Reply_messasge = 'ยินดีรับใช้ครับบ ^^ '.format(Text)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "โอเค" in message :
            Reply_messasge = 'ยินดีรับใช้ครับบ ^^ '.format(Text)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "ครับ" in message :
            Reply_messasge = 'เข้าใจแล้วใช่ไหม  '.format(Text)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "นับ" in message :
            Reply_messasge = 'หนึ่ง สอง สาม ปลาฉลาดขึ้นบก  '.format(Text)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "รัก" in message :
            Reply_messasge = 'LOVE ^^  '.format(Text)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "แฟน" in message :
            Reply_messasge = 'แอบชอบคุณอยู่นะ  '.format(Text)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "ตอบช้า" in message :
            Reply_messasge = 'บอทขอโทษษ ไม่โกรธนะคนดี  '.format(Text)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "ใช่" in message :
            Reply_messasge = 'คนนี้ใช่เลย '.format(Text)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "หิวข้าว" in message :
            Reply_messasge = 'บอทก็หิวเหมือนกันน '.format(Text)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "หิว" in message :
            Reply_messasge = 'บอทก็หิวเหมือนกันน '.format(Text)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "ข้าว" in message :
            Reply_messasge = 'กำลังหิวเลยยครับ '.format(Text)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "ไปหาอะไรกิน" in message :
            Reply_messasge = 'หิวที่สุดเลย '.format(Text)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "หรอ" in message :
            Reply_messasge = 'จริงๆนะ '.format(Text)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "ไม่" in message :
            Reply_messasge = 'อยู่ด้วยกันก่อนนะ'.format(Text)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "เค" in message :
            Reply_messasge = 'ยินดีรับใช้ครับบ ^^  '.format(Text)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "เก่ง" in message :
            Reply_messasge = 'ขอบคุณครับบ ^^  '.format(Text)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "ว้าว" in message :
            Reply_messasge = 'สุดยอดไปเลยย  '.format(Text)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "จริง" in message :
            Reply_messasge = 'ก็ตอบได้หมดนะ :)  '.format(Text)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "สุดยอด" in message :
            Reply_messasge = 'ก็ตอบได้หมดนะ :)  '.format(Text)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)



    elif request.method == 'GET' :
        return 'this is method GET!!!' , 500

    else:
        abort(400)

@app.route('/')
def hello():
    return 'hello world book',500

def ReplyMessage(Reply_token, TextMessage, Line_Acees_Token):
    LINE_API = 'https://api.line.me/v2/bot/message/reply'

    Authorization = 'Bearer {}'.format(Line_Acees_Token) ##ที่ยาวๆ
    print(Authorization)
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization':Authorization
    }

    data = {
        "replyToken":Reply_token,
        "messages":[{
            "type":"text",
            "text":TextMessage
        }]
    }

    data = json.dumps(data) ## dump dict >> Json Object
    r = requests.post(LINE_API, headers=headers, data=data) 
    return 500