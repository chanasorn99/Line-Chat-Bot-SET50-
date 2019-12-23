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
     	 #elif "หุ้น" in message :
          # Reply_messasge = 'ตรวจสอบหุ้น set50 ได้ที่ลิงค์นี้ \n https://marketdata.set.or.th/mkt/sectorquotation.do?sector=SET50&language=th&country=TH \nการลงทุนมีความเสี่ยง ผู้ลงทุนควรศึกษาข้อมูลก่อนการตัดสินใจลงทุน'.format(Text)
 		#ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
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

     	#wordwithstock #แก้ไขเพิ่มคำครั้งที่001
     	#WordwithStock
        elif "ลำไย" in message :
            Reply_messasge = 'กำไรแล้วหรอ'.format(Text)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "ซื้อควาย" in message :
            Reply_messasge = 'ถ้ามั่นใจก็ลองได้เลยยยง'.format(Text)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "ขายหมู" in message :
            Reply_messasge = 'ขึ้นไวจริง ๆ เลยราคาตอนนี้'.format(Text)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "ปู่" in message :
            Reply_messasge = 'ตลาด SET ยังไงละ'.format(Text)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)   	
     	   
        elif "ตกรถ" in message :
            Reply_messasge = 'ตามไม่ทันแล้วจ้า พี่จ๋าไวจริง ๆ'.format(Text)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        elif "ขึ้นรถ" in message :
            Reply_messasge = 'เอาละเตรียมตัวไว้เลย'.format(Text)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        elif "ติดดอย" in message :
            Reply_messasge = 'แย่ละทำไงดีซื้อมาแพง ขายไม่ทันแล้วจ้าาา'.format(Text)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        elif "หลุดดอย" in message :
            Reply_messasge = 'ในที่สุดก็รอดด นึกว่าจะขาดทุนสะแล้ว'.format(Text)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        elif "เคาะ" in message :
                    Reply_messasge = 'เอามาเลยจะซื้อ'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        elif "bid" in message :
                    Reply_messasge = 'ตั้งซื้อ'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        elif "offer" in message :
                    Reply_messasge = 'ตั้งขาย'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        elif "กำแพงหนา" in message :
                    Reply_messasge = 'Volume เยอะ'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        elif "เขื่อนแตก" in message :
                    Reply_messasge = 'Volume บางกว่าอีกั่งทำให้ราคาทะลุ'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        elif "ลาก" in message :
                    Reply_messasge = 'การซื้อทำให้ราคาสูง'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        elif "ทุบ" in message :
                    Reply_messasge = 'การเทราคาให้ต่ำ'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        elif "จ้าว" in message :
                    Reply_messasge = 'นักลงทุนรายใหญ่'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        elif "หรั่ง" in message :
                    Reply_messasge = 'นักลงทุนต่างชาติ'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        elif "ปอป" in message :
                    Reply_messasge = 'กลุ่มบัญชีบริษัทหลักทรัพย์'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        elif "เม่า" in message :
                    Reply_messasge = 'นักลงทุนรายย่อย'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        elif "แก๊ง 4 โมง" in message :
                    Reply_messasge = 'นอมินีที่มองไม่เห็น แต่ทุบถูกเวลา'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        elif "กระสุน" in message :
                    Reply_messasge = 'เงินที่เหลือในบัญชีโบรก ที่ยังสามารถซื้อได้'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        elif "ปอด" in message :
                    Reply_messasge = 'พอร์ตโฟลิโอ'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        elif "เต็มปอด" in message :
                    Reply_messasge = 'มีเงินเท่าไหร่ ซื้อหุ้นเต็มโควต้า'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        elif "ล้างปอด" in message :
                    Reply_messasge = 'เทขายหุ้นตัวเองจนพอร์ตโฟลิโอโล่งไม่เหลือแม้แต่บาทเดียว'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        elif "พวกวีไอ" in message :
                    Reply_messasge = 'กลุ่มคนที่เน้นการประเมินมูลค่าของธุรกิจเป็นหลัก'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        elif "พวกเทคนิค" in message :
                    Reply_messasge = 'กลุ่มคนที่เน้นการใช้เครื่องมือความน่าจะเป็นทางคณิตศาสตร์ในการหาจังหวะ ซื้อ-ขาย เป็นหลัก'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        elif "หุ้นปั่น" in message :
                    Reply_messasge = 'หุ้นที่จ้าวสิงอยู่ ควบคุมและทำราคา'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        elif "หุ้นพื้นฐาน" in message :
                    Reply_messasge = 'หุ้นที่ธุรกิจแข็งแกร่ง'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        elif "ติดคุก" in message :
                    Reply_messasge = 'หุ้นที่ กลต. ประกาศออกมาติด Cash Balance'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        elif "ตลก" in message :
                    Reply_messasge = 'การแซวของรายย่อยกับชื่อของ กลต.'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        elif "ปลั๊กหลุด" in message :
                    Reply_messasge = 'การหยุดการซื้อขายระหว่างวันไปดื้อๆ ทั้งตลาด'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        elif "บักโกรก" in message :
                    Reply_messasge = 'ขาดทุนหมดแล้วว'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        elif "โกย" in message :
                    Reply_messasge = 'เป็นการรีบเทขายหุ้นที่ถืออยู่ เกิด Panic ในตลาด'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        elif "ต้มกบ" in message :
                    Reply_messasge = 'การล่อซื้อให้ตายใจ เมื่อโดดเข้าหม้อแล้ว ค่อยๆ เร่งไฟ ตายคาหม้อ เพื่อสูบเอากำไรจากรายย่อย'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        elif "เด้ง" in message :
                    Reply_messasge = 'กำไร 100%'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        elif "ลิ่ง" in message :
                    Reply_messasge = 'ราคาหุ้นตัวนั้นๆ พุ่งสูงสุดเท่าที่เคยทำมา'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        elif "ฟลอร์" in message :
                    Reply_messasge = 'ราคาหุ้นตัวนั้นๆ ดิ่งลงสุดเท่าที่เคยทำมา'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        elif  "ไม้" in message :
                    Reply_messasge = 'การนับครั้งในการซื้อหุ้นตัวนั้นๆ'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        elif "เทิร์น ลาว" in message :
                    Reply_messasge = 'หุ้นที่ราคาดิ่งอยู่แล้ววกกลับขึ้นมา (จุดเปลี่ยนของชีวิต)'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        elif "เห็บฉลาม" in message :
                    Reply_messasge = 'นั่งรถคันเดียวกันกับรายใหญ่ และรายใหญ่เตรียมลากราคาขึ้น'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        elif "ปอดแดง" in message :
                    Reply_messasge = 'พอร์ตขาดทุน'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        elif "ปอดเขียว" in message :
                    Reply_messasge = 'พอร์ตกำไร'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        elif "ปอดแหก" in message :
                    Reply_messasge = 'พอร์ตขาดทุนหนัก'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        elif "จบรอบ" in message :
                    Reply_messasge = 'หมายถึงหุ้นที่มีราคาขึ้นมาจนสูงแล้ว ปรับตัวลงเป็นการจบรอบคือรายใหญ่ขายหุ้นไปจนหมดแล้วจะไม่มีข่าวอะไรให้ตื่นเต้นอีก'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        elif "วงใน" in message :
                    Reply_messasge = 'Insider ข้อมูลที่ยังไม่ปรากฎต่อสาธารณะ คนที่รู้ข้อมูลเหล่านี้เรียกว่าพวกวงใน มักจะอยู่ในอุตสาหกรรมนั้นๆ หรือเป็น ญาติ'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        elif "ตลาดกระทิง" in message :
                    Reply_messasge = 'ภาวะตลาดหุ้นที่ราคาหลักทรัพย์โดยทั่วไปมีระดับสูงขึ้นอย่างต่อเนื่องเป็นระยะเวลายาวนานไม่น้อยกว่า 2-3 เดือน'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        elif "ตลาดหมี" in message :
                    Reply_messasge = 'ภาวะตลาดหุ้นที่ราคาหลักทรัพย์โดยทั่วไปมีระดับที่ลดต่ำลงอย่างต่อเนื่องเป็นเวลายาวนาน และปริมาณการซื้อขายก็มีน้อย เปรียบเสมือนการเคลื่อนไหวของหมีที่อืดอาดเชื่องช้า'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        elif "Stars" in message :
                    Reply_messasge = 'กลุ่มอัตราการเจริญเติบโตสูงและส่วนแบ่งตลาดสูง'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        elif "cash cow" in message :
                    Reply_messasge = 'กลุ่มอัตราการเจริญเติบโตต่ำ แต่ส่วนแบ่งตลาดสูง'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        elif "dog" in message :
                    Reply_messasge = 'กลุ่มอัตราการเจริญเติบโตต่ำ และส่วนแบ่งการตลาดต่ำ '.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

  		#Trading terminology
        elif "Prior" in message :
                    Reply_messasge = 'ราคาปิดของวันก่อนหน้า'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "Open" in message :
                    Reply_messasge = 'ราคาเปิด'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "High" in message :
                    Reply_messasge = 'ราคาสูงสุด'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "Low" in message :
                    Reply_messasge = 'ราคาต่ำสุด'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token) 
        elif "Close" in message :
                    Reply_messasge = 'ราคาปิด'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "Change" in message :
                    Reply_messasge = 'การเปรียบเทียบราคาปิด กับ ราคาปิดของวันก่อนหน้า'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)           
        elif "Average" in message :
                    Reply_messasge = 'คำนวณราคาเฉลี่ยของหลักทรัพย์ที่น่าสนใจ'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "Volume" in message :
                    Reply_messasge = 'ปริมาณการซื้อขายหลักทรัพย์'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "Value" in message :
                    Reply_messasge = 'มูลค่าการซื้อขายหลักทรัพย์ ที่เกิดจากการรวบรวมมูลค่าซื้อขายที่เกิดขึ้นในทุกระดับราคา'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

                    #Financial ratio
        elif "Current Ratio" in message :
                    Reply_messasge = 'อัตราสภาพคล่อง เป็นอัตราส่วนที่ใช้ชี้ความสามารถของบริษัทที่จะใช้คืนหนี้ระยะสั้นเมื่อถึงกำหนด'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "Quick Ratio" in message :
                    Reply_messasge = 'สินทรัพย์หมุนเวียนที่สามารถเปลี่ยนเป็นเงินสดได้ไวดังนั้นจึงต้องหักสินค้าคงเหลือออก'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "Account Receivable Turnover" in message :
                    Reply_messasge = 'การบริหารลูกหนี้การค้าได้ดีเพียงใดโดยค่าที่คำนวณออกมาได้จะมีหน่วยเป็นรอบหากได้จำนวนรอบที่มากแสดงว่ามีการหมุนเวียนลูกหนี้การค้าได้หลายรอบใน 1 ปี'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "Day Receive" in message :
                    Reply_messasge = 'ระยะเวลาเก็บหนี้โดยเฉลี่ย'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token) 
        elif "Inventory Turnover" in message :
                    Reply_messasge = 'ระยะเวลาผลิตไปจนขายสินค้าได้โดยเฉลี่ยนานหรือสั้น'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "Debt to Equity" in message :
                    Reply_messasge = 'กิจการใช้ทุนในส่วนของหนี้สินหรือส่วนของผู้ถือหุ้นมากกว่ากัน'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)           
        elif "Net Profit Margin" in message :
                    Reply_messasge = 'ความสามารถในการทำกำไรสุทธิของกิจการ'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "Return on Asset" in message :
                    Reply_messasge = 'การวัดประสิทธิภาพการทำกำไรจากสินทรัพย์ทั้งหมดที่มีอยู่'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "Return on Equity" in message :
                    Reply_messasge = 'ผลตอบแทนในส่วนของผู้ถือหุ้นว่าเงินทุนที่ลงทุนไปให้ผลตอบแทนเท่าไหร่'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "P/E Ratio" in message :
                    Reply_messasge = 'ราคาหุ้นต่อกำไรสุทธิ 1 บาท'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "สูตร Current Ratio" in message :
                    Reply_messasge = 'สินทรัพย์หมุนเวียน ต่อ หนี้สินหมุนเวียน'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "สูตร Account Receivable Turnover" in message :
                    Reply_messasge = 'ยอดขายเชื่อ ต่อ ลูกหนี้การค้า'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "สูตร Inventory Turnover" in message :
                    Reply_messasge = 'ต้นทุนขาย ต่อ สินค้าคงเหลือ'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token) 
        elif "สูตร Net Profit Margin" in message :
                    Reply_messasge = 'กำไรสุทธิ*100 ต่อ ยอดขาย'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "สูตร Return on Equity" in message :
                    Reply_messasge = 'กำไรสุทธิ*100 ต่อ ส่วนของผู้ถือหุ้น'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)           
        elif "สูตร Quick Ratio" in message :
                    Reply_messasge = '(สินทรัพย์หมุนเวียน-สินค้าคงเหลือ-ค่าใช้จ่ายล่วงหน้า) ต่อ หนี้สินหมุนเวียน'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "สูตร Day Receive" in message :
                    Reply_messasge = '365 ต่อ Account Receivable Turnover'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "สูตร Debt to Equity" in message :
                    Reply_messasge = 'หนี้สินรวม ต่อ ส่วนของผู้ถือหุ้น'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "สูตร Return on Asset" in message :
                    Reply_messasge = 'กำไรสุทธิ*100 ต่อ สินทรัพย์รวม'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
		
		#List Stock News 
        elif "ข่าวหุ้นADVANC" in message :
                    Reply_messasge = 'ข่าวที่เกี่ยวข้องกับบริษัท แอดวานซ์ อินโฟร์ เซอร์วิส จำกัด (มหาชน) ณขณะนี้ \n https://www.ryt9.com/tag/ADVANC'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "ข่าวหุ้นAOT" in message :
                    Reply_messasge = 'ข่าวที่เกี่ยวข้องบริษัท ท่าอากาศยานไทย จำกัด (มหาชน) \n https://www.ryt9.com/tag/AOT'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
 		
        elif "ข่าวหุ้นAWC" in message :
                    Reply_messasge = 'ข่าวที่เกี่ยวข้องบริษัท แอสเสท เวิรด์ คอร์ป จำกัด (มหาชน) ณขณะนี้ \n https://www.ryt9.com/tag/%28AWC%29/ '.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
 		
        elif "ข่าวหุ้นBANPU" in message :
                    Reply_messasge = 'ข่าวที่เกี่ยวข้องบริษัท บ้านปู จำกัด (มหาชน) ณขณะนี้ \n https://www.ryt9.com/tag/BANPU'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
 		
        elif "ข่าวหุ้นBBL" in message :
                    Reply_messasge = 'ข่าวที่เกี่ยวข้องธนาคารกรุงเทพ จำกัด (มหาชน) ณขณะนี้ \n https://www.ryt9.com/tag/BBL'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
 		
        elif "ข่าวหุ้นBDMS" in message :
                    Reply_messasge = 'ข่าวที่เกี่ยวข้องบริษัท กรุงเทพดุสิตเวชการ จำกัด(มหาชน) ณขณะนี้ \n  https://www.ryt9.com/tag/BDMS'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "ข่าวหุ้นBEM" in message :
                    Reply_messasge = 'ข่าวที่เกี่ยวข้องบริษัท ทางด่วนและรถไฟฟ้ากรุงเทพ จำกัด (มหาชน) ณขณะนี้ \n  https://www.ryt9.com/tag/BEM'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "ข่าวหุ้นBGRIM" in message :
                    Reply_messasge = 'ข่าวที่เกี่ยวข้องบริษัท บี.กริม เพาเวอร์ จำกัด (มหาชน) ณขณะนี้ \n  https://www.ryt9.com/tag/BGRIM'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "ข่าวหุ้นBH" in message :
                    Reply_messasge = 'ข่าวที่เกี่ยวข้องบริษัท โรงพยาบาลบำรุงราษฎร์ จำกัด (มหาชน) ณขณะนี้ \n  https://www.ryt9.com/tag/BH'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "ข่าวหุ้นBJC" in message :
                    Reply_messasge = 'ข่าวที่เกี่ยวข้องบริษัท เบอร์ลี่ ยุคเกอร์ จำกัด (มหาชน) ณขณะนี้ \n  https://www.ryt9.com/tag/BJC'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "ข่าวหุ้นBPP" in message :
                    Reply_messasge = 'ข่าวที่เกี่ยวข้องบริษัท บ้านปู เพาเวอร์ จำกัด (มหาชน) ณขณะนี้ \n  https://www.ryt9.com/tag/BPP'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "ข่าวหุ้นBTS" in message :
                    Reply_messasge = 'ข่าวที่เกี่ยวข้องบริษัท บีทีเอส กรุ๊ป โฮลดิ้งส์ จำกัด (มหาชน) ณขณะนี้ \n  https://www.ryt9.com/tag/BTS'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "ข่าวหุ้นCBG" in message :
                    Reply_messasge = 'ข่าวที่เกี่ยวข้องบริษัท คาราบาวกรุ๊ป จำกัด (มหาชน) ณขณะนี้ \n  https://www.ryt9.com/tag/CBG'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "ข่าวหุ้นCPALL" in message :
                    Reply_messasge = 'ข่าวที่เกี่ยวข้องบริษัท ซีพี ออลล์ จำกัด (มหาชน) ณขณะนี้ \n  https://www.ryt9.com/tag/CPALL'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "ข่าวหุ้นCPF" in message :
                    Reply_messasge = 'ข่าวที่เกี่ยวข้องบริษัท เจริญโภคภัณฑ์อาหาร จำกัด (มหาชน) ณขณะนี้ \n  https://www.ryt9.com/tag/CPF'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "ข่าวหุ้นCPN" in message :
                    Reply_messasge = 'ข่าวที่เกี่ยวข้องบริษัท เซ็นทรัลพัฒนา จำกัด (มหาชน) ณขณะนี้ \n  https://www.ryt9.com/tag/CPN'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "ข่าวหุ้นDELTA" in message :
                    Reply_messasge = 'ข่าวที่เกี่ยวข้องบริษัทเดลต้า อีเลคโทรนิคส์ (ประเทศไทย) จำกัด (มหาชน) ณขณะนี้ \n https://www.ryt9.com/tag/DELTA'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "ข่าวหุ้นDTAC" in message :
                    Reply_messasge = 'ข่าวที่เกี่ยวข้องบริษัท โทเทิ่ล แอ็คเซ็ส คอมมูนิเคชั่น จำกัด (มหาชน) ณขณะนี้ \n https://www.ryt9.com/tag/DTAC'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "ข่าวหุ้นEA" in message :
                    Reply_messasge = 'ข่าวที่เกี่ยวข้องบริษัท พลังงานบริสุทธิ์ จำกัด (มหาชน) ณขณะนี้ \n https://www.ryt9.com/tag/EA'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "ข่าวหุ้นข่าวหุ้นEGCO" in message :
                    Reply_messasge = 'ข่าวที่เกี่ยวข้องบริษัท ผลิตไฟฟ้า จำกัด (มหาชน) ณขณะนี้ \n https://www.ryt9.com/tag/EGCO'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "ข่าวหุ้นCLOBAL" in message :
                    Reply_messasge = 'ข่าวที่เกี่ยวข้องบริษัท สยามโกลบอลเฮ้าส์ จำกัด (มหาชน) ณขณะนี้ \n https://www.ryt9.com/tag/CLOBAL'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "ข่าวหุ้นGPSC" in message :
                    Reply_messasge = 'ข่าวที่เกี่ยวข้องบริษัท โกลบอล เพาเวอร์ ซินเนอร์ยี่ จำกัด (มหาชน) ณขณะนี้ \n https://www.ryt9.com/tag/GPSC'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "ข่าวหุ้นGULF" in message :
                    Reply_messasge = 'ข่าวที่เกี่ยวข้องบริษัท กัลฟ์ เอ็นเนอร์จี ดีเวลลอปเมนท์ จำกัด (มหาชน) ณขณะนี้ \n https://www.ryt9.com/tag/GULF'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "ข่าวหุ้นHMPRO" in message :
                    Reply_messasge = 'ข่าวที่เกี่ยวข้องบริษัท โฮม โปรดักส์ เซ็นเตอร์ จำกัด (มหาชน) ณขณะนี้ \n https://www.ryt9.com/tag/HMPRO'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "ข่าวหุ้นINTUCH" in message :
                    Reply_messasge = 'ข่าวที่เกี่ยวข้องบริษัท อินทัช โฮลดิ้งส์ จำกัด (มหาชน) ณขณะ \n  https://www.ryt9.com/tag/INTUCH'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "ข่าวหุ้นIRPC" in message :
                    Reply_messasge = 'ข่าวที่เกี่ยวข้อง บริษัท ไออาร์พีซี จำกัด (มหาชน) ณขณะนี้ \n https://www.ryt9.com/tag/IRPCข่าวที่เกี่ยวข้องบริษัท อินทัช โฮลดิ้งส์ จำกัด (มหาชน) ณขณะ \n INTUCH'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "ข่าวหุ้นIVL" in message :
                    Reply_messasge = 'ข่าวที่เกี่ยวข้องบริษัท อินโดรามา เวนเจอร์ส จำกัด (มหาชน) ณขณะนี้ \n https://www.ryt9.com/tag/IVL'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "ข่าวหุ้นKBANK" in message :
                    Reply_messasge = 'ข่าวที่เกี่ยวข้องธนาคารกสิกรไทย จำกัด (มหาชน) ณขณะนี้ \n https://www.ryt9.com/tag/KBANK'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "ข่าวหุ้นKTB" in message :
                    Reply_messasge = 'ข่าวที่เกี่ยวข้องธนาคารกรุงไทย จำกัด (มหาชน) ณขณะนี้ \n https://www.ryt9.com/tag/KTB'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)            	
        elif "ข่าวหุ้นKTC" in message :
                    Reply_messasge = 'ข่าวที่เกี่ยวข้องบริษัท บัตรกรุงไทย จำกัด (มหาชน) ณขณะนี้ \n https://www.ryt9.com/tag/KTC'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "ข่าวหุ้นLH" in message :
                    Reply_messasge = 'ข่าวที่เกี่ยวข้องบริษัทแลนด์แอนด์เฮ้าส์ จำกัด (มหาชน) ณขณะนี้ \n https://www.ryt9.com/tag/LH'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "ข่าวหุ้นMINT" in message :
                    Reply_messasge = 'ข่าวที่เกี่ยวข้องบริษัท ไมเนอร์ อินเตอร์เนชั่นแนล จำกัด (มหาชน) ณขณะนี้ \n https://www.ryt9.com/tag/MINT'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "ข่าวหุ้นMTC" in message :
                    Reply_messasge = 'ข่าวที่เกี่ยวข้องบริษัท เมืองไทย แคปปิตอล จำกัด (มหาชน) ณขณะนี้ \n https://www.ryt9.com/tag/MTC'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "ข่าวหุ้นOSP" in message :
                    Reply_messasge = 'ข่าวที่เกี่ยวข้องบริษัท โอสถสภา จำกัด (มหาชน) ณขณะนี้ \n https://www.ryt9.com/tag/OS'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "ข่าวหุ้นPTT" in message :
                    Reply_messasge = 'ข่าวที่เกี่ยวข้องบริษัท ปตท. จำกัด (มหาชน) ณขณะนี้ \n https://www.ryt9.com/tag/PTT'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "ข่าวหุ้นPTTEP" in message :
                    Reply_messasge = 'ข่าวที่เกี่ยวข้องบริษัท ปตท. สำรวจและผลิตปิโตรเลียม จำกัด (มหาชน) ณขณะนี้ \n  https://www.ryt9.com/tag/PTTEP'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "ข่าวหุ้นPTTGC" in message :
                    Reply_messasge = 'ข่าวที่เกี่ยวข้องบริษัท พีทีที โกลบอล เคมิคอล จำกัด (มหาชน) ณขณะนี้ \n  https://www.ryt9.com/tag/PTTGC'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "ข่าวหุ้นRATCH" in message :
                    Reply_messasge = 'ข่าวที่เกี่ยวข้องบริษัท ราช กรุ๊ป จำกัด (มหาชน) ณขณะนี้ \n  https://www.ryt9.com/tag/RATCH'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "ข่าวหุ้นROBINS" in message :
                    Reply_messasge = 'ข่าวที่เกี่ยวข้องบริษัท โรบินสัน จำกัด (มหาชน) ณขณะนี้ \n  https://www.ryt9.com/tag/ROBINS'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "ข่าวหุ้นSAWAD" in message :
                    Reply_messasge = 'ข่าวที่เกี่ยวข้องบริษัท ศรีสวัสดิ์ คอร์ปอเรชั่น จำกัด (มหาชน) ณขณะนี้ \n  https://www.ryt9.com/tag/SAWAD'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "ข่าวหุ้นSCB" in message :
                    Reply_messasge = 'ข่าวที่เกี่ยวข้องธนาคารไทยพาณิชย์ จำกัด (มหาชน) ณขณะนี้ \n  https://www.ryt9.com/tag/SCB'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "ข่าวหุ้นSCC" in message :
                    Reply_messasge = 'ข่าวที่เกี่ยวข้องบริษัท ปูนซิเมนต์ไทย จำกัด(มหาชน) ณขณะนี้ \n  https://www.ryt9.com/tag/SCC'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "ข่าวหุ้นTTCAP" in message :
                    Reply_messasge = 'ข่าวที่เกี่ยวข้องบริษัท ทุนธนชาต จำกัด (มหาชน) ณขณะนี้ \n  https://www.ryt9.com/tag/TTCAP'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "ข่าวหุ้นTISCO" in message :
                    Reply_messasge = 'ข่าวที่เกี่ยวข้องบริษัท ทิสโก้ไฟแนนเชียลกรุ๊ป จำกัด (มหาชน) ณขณะนี้ \n  https://www.ryt9.com/tag/TISCO'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "ข่าวหุ้นTMB" in message :
                    Reply_messasge = 'ข่าวที่เกี่ยวข้องธนาคารทหารไทย จำกัด (มหาชน) ณขณะนี้ \n  https://www.ryt9.com/tag/TMB'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "ข่าวหุ้นTOA" in message :
                    Reply_messasge = 'ข่าวที่เกี่ยวข้องบริษัท ทีโอเอ เพ้นท์ (ประเทศไทย) จำกัด (มหาชน) ณขณะนี้ \n  https://www.ryt9.com/tag/TOA'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "ข่าวหุ้นTOP" in message :
                    Reply_messasge = 'ข่าวที่เกี่ยวข้องบริษัท ไทยออยล์ จำกัด (มหาชน) ณขณะนี้ \n  https://www.ryt9.com/tag/TOP'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "ข่าวหุ้นTRUE" in message :
                    Reply_messasge = 'ข่าวที่เกี่ยวข้องบริษัท ทรู คอร์ปอเรชั่น จำกัด (มหาชน) ณขณะนี้ \n  https://www.ryt9.com/tag/TRUE'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "ข่าวหุ้นTU" in message :
                    Reply_messasge = 'ข่าวที่เกี่ยวข้องบริษัท ไทยยูเนี่ยน กรุ๊ป จำกัด (มหาชน) ณขณะนี้ \n  https://www.ryt9.com/tag/TU'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "ข่าวหุ้นWHA" in message :
                    Reply_messasge = 'ข่าวที่เกี่ยวข้องบริษัท ดับบลิวเอชเอ คอร์ปอเรชั่น จำกัด (มหาชน) ณขณะนี้ \n  https://www.ryt9.com/tag/WHA'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
      


        #STOCK NEW
        
        elif "ข่าวตลาด" in message :
                    Reply_messasge = 'ข่าวหุ้นไทย ณขณะนี้ \n https://www.ryt9.com/tag/%E0%B8%AB%E0%B8%B8%E0%B9%89%E0%B8%99%E0%B9%84%E0%B8%97%E0%B8%A2'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
 		
        elif "ข่าว" in message :
                    Reply_messasge = 'ข่าวหุ้นไทย ณขณะนี้ \n https://www.ryt9.com/tag/%E0%B8%AB%E0%B8%B8%E0%B9%89%E0%B8%99%E0%B9%84%E0%B8%97%E0%B8%A2'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
 		
        elif "ข่าวหุ้นไทย" in message :
                    Reply_messasge = 'ข่าวหุ้นไทย ณขณะนี้ \n https://www.ryt9.com/tag/%E0%B8%AB%E0%B8%B8%E0%B9%89%E0%B8%99%E0%B9%84%E0%B8%97%E0%B8%A2'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
 		
        elif "ภาพรวมตลาดหุ้นไทย" in message :
                    Reply_messasge = 'ข่าวหุ้นไทย ณขณะนี้ \n https://www.ryt9.com/tag/%E0%B8%AB%E0%B8%B8%E0%B9%89%E0%B8%99%E0%B9%84%E0%B8%97%E0%B8%A2'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
 		
        elif "ภาพรวมตลาดหุ้นไทย" in message :
                    Reply_messasge = 'ข่าวหุ้นไทย ณขณะนี้ \n https://www.ryt9.com/tag/%E0%B8%AB%E0%B8%B8%E0%B9%89%E0%B8%99%E0%B9%84%E0%B8%97%E0%B8%A2'.format(Text)
                    ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
 		
 		 
       
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