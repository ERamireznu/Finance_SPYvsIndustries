#15/04/24 adding more info; getting ready for use as import file
#08/06/24: all industries data refresh; now 1626 comps, before app. 1033 comps
#v01: 04/02/26
#-------------------all industries
A01 = ['NTR','CTVA','CF','FMC','MOS','ICL','SMG'] #Basic Mats - Agricultural inputs
A02 = ['AA','CSTM','CENX','KALU'] #Basic Mats - Aluminum
A03 = ['CRH','VMC','MLM','AMRZ','JHX','CX','EXP','KNF','TTAM','USLM','TGLS'] #Basic Mats - Build mats
A04 = ['DOW','CE','MEOH','OLN','HUN','TROX','REX'] #Basic Mats - Chemicals
A05 = ['AMR','HCC','SXC','METC','AREC'] #Basic Mats - Coking coal
A06 = ['SCCO','FCX','ERO','HBM','TGB','IE'] #Basic Mats - Copper
A07 = ['NEM','AEM','B','WPM','AU','GFI','FNV','KGC','RGLD','PAAS','AGI','CDE','HMY','EQX','IAG'] #Basic Mats - Gold
A08 = ['SSD','UFPI','WFG','NWGL','BCC'] #Basic Mats - Lumber & Wood prod
A09 = ['BHP','RIO','VALE','TECK','MP','USAR','EMAT','SKE','ALM','MTRN'] #Basic Mats - Other Indus Metal & Min
A10 = ['TFPM','HL','BVN','SBSW','ASM','MUX','SLSR','PPTA'] #Basic Mats - Other Precious Metal & Min
A11 = ['SUZ','SLVM','CLW','MERC'] #Basic Mats - Paper & Paper prods
A12 = ['AG','EXK','SVM','NEWP'] #Basic Mats - Silver
A13 = ['LIN','SHW','ECL','APD','DD','LYB','PPG','IFF','WLK','RPM','ALB','EMN','AXTA','SQM','ESI'] #Basic Mats - Specialty Chemicals
A14 = ['NUE','MT','STLD','PKX','RS','TX','CLF','CMC','SIM','GGB','SID','WS'] #Basic Mats - Steel
B01 = ['APP','OMC','TTD','WPP','MGNI','DV','SBET','ZD','STGW','CCO'] #Comm Services - Advertising Agencies
B02 = ['NXST','TGNA','SBGI','NMAX','GTN','FUBO','SSP','IHRT','CURI'] #Comm Services - Broadcasting
B03 = ['NTES','EA','RBLX','TTWO','PLTK','GRVY'] #Comm Services - Electro Gaming & Multi
B04 = ['NFLX','DIS','LYV','WBD','TKO','FWONA','FOX','FOXA','FWONK','NWS','NWSA','WMG','SIRI','ROKU','PSKY','LLYVK','LLYVA'] #Comm Services - Entertainment
B05 = ['GOOGL','GOOG','META','SPOT','PINS','BIDU','RDDT','SNAP','BILI','TME','MTCH','ZG','Z','BZ'] #Comm Services - Internet Content & Info
B06 = ['PSO','NYT','WLY','SCHL','TDAY'] #Comm Services - Publishing
B07 = ['TMUS','VZ','T','CMCSA','AMX','VOD','CHTR','BCE','CHT','SATS','TLK','TU','RCI','VIV','SKM'] #Comm Services - Telecom Services
C01 = ['RL','LEVI','PVH','GIL','VFC','COLM','KTB','UAA','ZGN','UA','OXM','GOOS','FIGS','GIII'] #Cons Cyc - Apparel Manufacturing
C02 = ['TJX','ROST','LULU','BURL','GAP','ANF','URBN','AEO','BOOT','VSCO','CRI','BKE'] #Cons Cyc - Apparel Retail
C03 = ['CVNA','KMX','PAG','LAD','AN','ABG','GPI','RUSHA','BGSI','VVV','OPLN'] #Cons Cyc - Auto & Truck Dealer
C04 = ['TSLA','TM','VFS','HMC','RACE','STLA','F','GM','LI','NIO','RIVN','XPEV','LCID'] #Cons Cyc - Auto Manufacturers
C05 = ['ORLY','AZO','APTV','GPC','MGA','LKQ','ALV','BWA','GNTX','LEA','ALSN','MOD','MBLY','QS'] #Cons Cyc - Auto Parts
C06 = ['DDS','M','PLBL','KSS'] #Cons Cyc - Department Stores
C07 = ['NKE','DECK','ONON','BIRK','CROX','SHOO','WWW'] #Cons Cyc - Footwear & Accesories
C08 = ['SGI','SN','WHR','ALH','HNI','BOBS','TILE','MHK','MBC','MLKN','LEG','LZB'] #Cons Cyc - Furnis, Fixts, Applncs
C09 = ['FLUT','DKNG','CHDN','SGHC','ACEL','RSI','BRSL','CDRO'] #Cons Cyc - Gambling
C10 = ['HD','LOW','FND','HVT'] #Cons Cyc - Home Improvement Retail
C11 = ['AMZN','BABA','PDD','MELI','DASH','JD','CPNG','EBAY','SE','CHWY','CART','W'] #Cons Cyc - Internet Retail
C12 = ['HAS','AS','MAT','PLNT','YETI','GOLF','LTH','CALY','OSW','PTON','PRKS','FUN','MSGE'] #Cons Cyc - Leisure
C13 = ['MAR','HLT','HTHT','IHG','H','CHH','WH','ATAT'] #Cons Cyc - Lodging
C14 = ['TPR','CPRI','SIG','LUXE','REAL'] #Cons Cyc - Luxury Goods
C15 = ['SW','BALL','AVY','AMCR','PKG','IP','CCK','GPK','SON','REYN','SEE','SLGN','GEF'] #Cons Cyc - Packaging & Containers
C16 = ['ROL','SCI','HRB','BFAM','FTDR','ANDG','CSV'] #Cons Cyc - Personal Services
C17 = ['PII','BC','THO','DOO','PATK','HOG','LCII','WGO','MBUU','MCFT'] #Cons Cyc - Recreational Vehicles
C18 = ['DHI','LEN','NVR','PHM','TOL','TMHC','MTH','IBP','KBH','SKY','CVCO','TPH','MHO','GRBK'] #Cons Cyc - Residential Construction
C19 = ['LVS','MGM','CZR','WYNN','MTN','BYD','MLCO','HGV','RRR','VAC','MCRI','PENN'] #Cons Cyc - Resorts & Casinos
C20 = ['MCD','SBUX','CMG','YUM','YUMC','QSR','DRI','DPZ','TXRH','WING','CAVA','SHAK','BROS','EAT'] #Cons Cyc - Restaurants
C21 = ['TSCO','WSM','ULTA','DKS','BBY','CASY','BBWI','MUSA','FIVE','GME','MNSO','RH','ASO'] #Cons Cyc - Specialty Retail
C22 = ['AIN','UFI','CULP'] #Cons Cyc - Textile Manufacturing
C23 = ['BKNG','ABNB','TCOM','RCL','CCL','EXPE','VIK','MMYT','NCLH','TNL','CUK'] #Cons Cyc - Travel services
D01 = ['BUD','ABEV','STZ','FMX','TAP','SAM','CCU'] #Cons Def - Beverages - Brewers
D02 = ['KO','PEP','MNST','KDP','CCEP','KOF','CELH','PRMB','COKE'] #Cons Def - Beverages - Non Alcoholic
D03 = ['DEO','BF-A','BF-B','MGPI'] #Cons Def - Beverages - Wineries & Distilleries
D04 = ['MDLZ','HSY','TR'] #Cons Def - Confectioners
D05 = ['WMT','COST','TGT','DG','DLTR','BJ','OLLI'] #Cons Def - Discount Stores
D06 = ['EDU','TAL','LOPE','GHC','LRN','STRA','ATGE','MH','LAUR','PRDO','AFYA','COUR','UTI','PXED'] #Cons Def - Education & Training Services
D07 = ['ADM','TSN','BG','CALM','VITL','FDP','DOLE','AGRO','LND'] #Cons Def - Farm products
D08 = ['SYY','USFD','PFGC','ANDE','CHEF','UNFI','AVO','CVGW'] #Cons Def - Food Distribution
D09 = ['KR','ACI','SFM','GO','DNUT','WMK','IMKTA','NGVC'] #Cons Def - Grocery Stores
D10 = ['PG','UL','CL','EL','KVUE','KMB','CHD','CLX','ELF','IPAR','COTY'] #Cons Def - Household & Personal products
D11 = ['KHC','GIS','MKC','HRL','MICC','SJM','CAG','LW','CPB','PPC','SFD','BRBR','INGR','POST','FRPT','DAR','JBS','MZTI','FLO','CENT'] #Cons Def - Packaged Foods
D12 = ['PM','MO','BTI'] #Cons Def - Tobacco
E01 = ['NE','RIG','HP','SDRL','PTEN','BORR','PDS','SOC','NBR'] #Energy - Oil & Gas Drilling
E02 = ['COP','CNQ','EOG','OXY','FANG','WDS','DVN','EXE','CTRA','EQT','TPL','OVV','APA','AR','PR','RRC','CRK','CHRD','CNX','MTDR'] #Energy - Oil & Gas E&P
E03 = ['SLB','BKR','HAL','TS','FTI','WFRD','NOV','VAL','LB','KGS','SEI','TDW','LBRT','WHD','AROC','USAC','OII','EFXT','NESR','FLOC'] #Energy - Oil & Gas Equip & Serv
E04 = ['XOM','CVX','SHEL','TTE','BP','EQNR','PBR','SU','E','PBR-A','CVE','IMO','EC','YPF'] #Energy - Oil & Gas Integ
E05 = ['ENB','EPD','WMB','ET','OKE','LNG','KMI','TRP','MPLX','CQP','TRGP','PBA','VG','WES','PAGP','VNOM','PAA','AM','HESM','DTM'] #Energy - Oil & Gas Midstream
E06 = ['MPC','PSX','VLO','DINO','IEP','PBF','CSAN','UGP','SUN','DKL','CVI'] #Energy - Oil & Gas Ref & Mark
E07 = ['CNR','ARLP','BTU','NRP','HNRG','NC'] #Energy - Thermal coal
E08 = ['CCJ','NXE','UEC','DNN','UUUU','LEU','ISOU','URG','UROY'] #Energy - Uranium
F01 = ['BX','BLK','BN','KKR','APO','AMP','ARES','TROW','STT','RJF','PFG','CRBG','NTRS','CG','TPG','BEN','OWL','PHYS','BAM','PSLV'] #Financial - Asset Management
F02 = ['JPM','BAC','WFC','HSBC','RY','TD','MUFG','UBS','C','SAN','SMFG','BMO','BNS','ING','BBVA','CM','BK','BCS'] #Financial - Banks - Diversified
F03 = ['HDB','IBN','PNC','USB','NU','MFG','TFC','LYG','NWG','DB','ITUB','FITB','FCNCA','MTB','KB','HBAN','SHG','RF','CFG','BAP'] #Financial - Banks - Regional
F04 = ['MS','GS','SCHW','TW','LPLA','HOOD','NMR','IBKR','XP','JEF','FUTU','HLI','SF','EVR','IREN','CRCL','BMNR','FIGR','PJT','GLXY'] #Financial - Capital Markets
F05 = ['V','MA','AXP','PYPL','COF','SYF','ALLY','SOFI','AFRM'] #Financial - Credit Services
F06 = ['IX','FRHC','VOYA','HTH','TREE'] #Financial - Fin Conglomerates
F07 = ['SPGI','CME','ICE','MCO','MSCI','NDAQ','COIN','FDS','CBOE','TRU','MORN'] #Financial - Fin Data & Stock Exch
F08 = ['BRK-A','BRK-B','AIG','HIG','SLF','ACGL','BNT','AEG'] #Financial - Insurance - Diversified
F09 = ['MET','AFL','PUK','MFC','PRU','GL','UNM','PRI','JXN','LNC','FG','CNO','GNW','BHF'] #Financial - Insurance - Life
F10 = ['CB','PGR','TRV','ALL','MKL','CINF','WRB','L','CNA','AIZ','AFG','ORI','KNSL','RLI','THG','LMND'] #Financial - Insurance - Property & Casual
F11 = ['EG','RNR','RGA','SPNT','HG','GLRE','OXBR'] #Financial - Insurance - Reinsur
F12 = ['RYAN','FNF','AXS','FAF','ESNT','MTG','ACT','RDN','AGO','NMIH','EIG','AMSF','TIPT','ITIC','MBI'] #Financial - Insurance - Specialty
F13 = ['MRSH','AON','AJG','WTW','BRO','ERIE','NP','ARX','CRVL','BWIN'] #Financial - Insurance Brokers
F14 = ['RKT','PFSI','WD','UWMC','VEL','BETR','ONIT','LDI','GHI','BLNE','IOR'] #Financial - Mortgage finance
F15 = ['LION','XXI','DMII','CCCX','CEPF'] #Financial - Shell Companies
G01 = ['VRTX','REGN','MRNA','ONC','BNTX','ARGX','GMAB','RVMD','ROIV','IONS','ASND','BBIO','EXEL','SMMT','RNA','ALNY','RPRX','BMRN','INCY','INSM'] #Health - Biotech
G02 = ['TMO','DHR','IDXX','IQV','A','ILMN','MTD','ICLR','LH','WAT','DGX','RVTY','NTRA','MEDP','GH','CRL','QGEN','RDNT','SHC','EXAS'] #Health - Diagnost & Research
G03 = ['LLY','JNJ','MRK','ABBV','NVS','AZN','PFE','NVO','AMGN','SNY','BMY','GILD','GSK','BIIB'] #Health - Drug Manufcs - Gral
G04 = ['ZTS','TAK','HLN','VTRS','RDY','TEVA','UTHR','NBIX','RGC','ELAN','LNTH','ALKS','HIMS','AMRX','INDV','KNSA','PBH'] #Health - Drug Manufcs - Specialty & Generic
G05 = ['VEEV','TEM','HQY','DOCS','WAY','GDRX','TXG','PRVA','HNGE','HTFL','CERT','BTSG','TDOC','SDGR','OMCL','PHR','OMDA'] #Health - Health Info Services
G06 = ['UNH','ELV','CVS','CI','HUM','CNC','MOH'] #Health - Health plans
G07 = ['HCA','THC','FMS','UHS','ENSG','EHC','DVA','CHE','PACS','OPCH','BKD','CON','LFST','NHC','GRDN','ADUS','SEM'] #Health - Medical Care Facilities
G08 = ['ABT','MDT','SYK','BSX','EW','GEHC','PHG','DXCM','STE','ZBH','PODD','SNN','PEN','GMED','BIO','MASI','GKOS','BRKR','IRTC','TMDX'] #Health - Medical Devices
G09 = ['MCK','COR','CAH','HSIC','AHG','ACH'] #Health - Medical Distr
G10 = ['ISRG','BDX','MDLN','RMD','ALC','WST','HOLX','COO','SOLV','ALGN','BAX','ATR','RGEN','AVTR','BLCO','MMSI','TFX','NVST','STVN','ICUI'] #Health - Medical Instruments & Supps
G11 = ['HITI','PETS','RDGT','WGRX'] #Health - Pharmaceutical Retailers
H01 = ['GE','BA','RTX','LMT','NOC','GD','HWM','TDG','LHX','HEI','HEI-A','RKLB','AXON','ESLT','CW','WWD','BWXT','TXT'] #Industrials - Aerospace & Defense
H02 = ['DAL','RYAAY','UAL','LUV','LTM','AAL','ALK','CPA','SKYW','AERO','JBLU','ALGT'] #Industrials - Airlines
H03 = ['ASR','PAC','JOBY','OMAB','CAAP','UP','ASLE'] #Industrials - Airports & Air Serv
H04 = ['TT','CARR','JCI','CSL','BLDR','LII','MAS','WMS','OC','SPXC','AWI','AAON','FBIN','LPX','TREX','GFF','ROCK'] #Industrials - Build Prods & Equip
H05 = ['EBF','ACTG','ACCO','XRX'] #Industrials - Business Equip & Supps
H06 = ['HON','MMM','VMI','SEB','OTTR','TTI','DLX','MATW','BBU'] #Industrials - Conglomerates
H07 = ['VRSK','EFX','BAH','FCN','ICFI','HURN','CRAI','SBC'] #Industrials - Consulting Services
H08 = ['VRT','BE','HUBB','NVT','AEIS','AYI','POWL','ENS','EOSE','HAYW','PLUG','ATKR','TE','ENR','AMPX'] #Industrials - Electrical Equip & parts
H09 = ['PWR','FER','FIX','EME','MTZ','APG','J','BLD','ACM','STRL','DY','STN','TTEK','IESC','PRIM','FLR','ROAD','ACA','GVA','KBR'] #Industrials - Engineering & Constr
H10 = ['CAT','DE','PCAR','CNH','AGCO','OSK','TEX','ALG'] #Industrials - Farm & Heavy Cons Mach
H11 = ['GWW','FERG','FAST','WSO','QXO','POOL','CNM','WCC','AIT','SITE','REZI','MSM'] #Industrials - Indust Distribution
H12 = ['UPS','FDX','ZTO','JBHT','EXPD','CHRW','GXO','LSTR','HUBG'] #Industrials - Int Freight & Log
H13 = ['KEX','HAFN','MATX','SBLK','BWLP','ZIM','CMRE','DAC','NMM','ECO','GSL','SFL','CCEC','GNK','SB','PANL','ASC','HSHP','CMDB','ESEA'] #Industrials - Marine Shipping
H14 = ['ATI','MLI','ESAB','GPGI','WOR','CRS','PRLB','RYI','IIIN'] #Industrials - Metal Fabrica
H15 = ['VLTO','ZWS','FSS','ADUR','PCT','CECO','ERII'] #Industrials - Pollution & Treatm Ctrls
H16 = ['UNP','CP','CNI','CSX','NSC','WAB'] #Industrials - Railroads
H17 = ['URI','AER','FTAI','UHAL','UHAL-B','R','EQPT','AL','GATX','HRI','CAR','WSC','MGRC','HTZ','CTOS','PRG','WLFC'] #Industrials - Rental & Leasing Servs
H18 = ['ALLE','MSA','ADT','BCO','BRC','GEO','NSSC','CXW','EVLV','MG'] #Industrials - Security & Protect Servs
H19 = ['RELX','TRI','CTAS','CPRT','RTO','RBA','ARMK','AMTM','DLB','MMS','AZZ'] #Industrials - Specialty Business Servs
H20 = ['GEV','ETN','PH','EMR','ITW','CMI','AME','ROK','IR','SYM','OTIS','XYL','DOV','ITT','NDSN','PNR','IEX','GGG','RRX','DCI'] #Industrials - Specialty Indust Machine
H21 = ['RHI','TNET','NSP','MAN','KFY','BBSI','KFRC'] #Industrials - Staff & Employ Servs
H22 = ['SNA','SWK','LECO','TTC','RBC','TKR','KMT','HLMN'] #Industrials - Tools & Accessories
H23 = ['ODFL','XPO','TFII','SAIA','KNX','SNDR','ARCB','RXO','WERN','MRTN','HTLD'] #Industrials - Trucking
H24 = ['WM','RSG','WCN','GFL','CLH','CWST','NVRI'] #Industrials - Waste Management
H25 = ['BEEP'] #Industrials - Infrastructure Operations

I01 = ['VTMX','CCS','FOR','SDHC','SKYH','FPH','OZ'] #Real Estate - R E  Development
I02 = ['HHH','JOE','STRS'] #Real Estate - R E  Diversified
I03 = ['CSGP','CBRE','BEKE','FSV','JLL','COMP','CIGI','OPEN','CWK','NMRK','IHS','HBNB','EXPI'] #Real Estate - R E  Services
I04 = ['VICI','WPC','BNL','GNL','ESRT','SAFE','AAT','CTO'] #Real Estate - REIT - Diversified
I05 = ['WELL','VTR','DOC','OHI','HR','CTRE','SBRA','NHI','MPT','AHR','LTC'] #Real Estate - REIT - Health Facilities
I06 = ['HST','RHP','APLE','PK','SHO','DRH','PEB','RLJ','XHR','SVC','INN','CLDT'] #Real Estate - REIT - Hotel & Motel
I07 = ['PLD','PSA','EXR','REXR','LINE','CUBE','EGP','COLD','STAG','FR','TRNO','NSA','LXP'] #Real Estate - REIT - Industrial
I08 = ['NLY','STWD','AGNC','RITM','BXMT','DX','ARR','EFC','ABR','ARI','LADR','TWO','ORC','PMT','CIM','MFA','FBRT','BRSP','ADAM','RWT'] #Real Estate - REIT - Mortgage
I09 = ['ARE','BXP','CDP','VNO','CUZ','KRC','SLG','HIW','ESBA','DEI','JBGS','DEA','PDM','PKST','PSTL','BDN','HPP'] #Real Estate - REIT - Office
I10 = ['AVB','EQR','INVH','MAA','SUI','ESS','UDR','AMH','MRP','ELS','CPT','IRT'] #Real Estate - REIT - Residential
I11 = ['O','SPG','KIM','REG','FRT','NNN','BRX','ADC','EPRT','KRG','MAC','PECO','SKT','AKR','UE','FCPT','CURB','IVT'] #Real Estate - REIT - Retail
I12 = ['AMT','EQIX','CCI','DLR','WY','SBAC','IRM','GLPI','LAMR','RYN','FRMI','OUT','EPR'] #Real Estate - REIT - Specialty
J01 = ['CSCO','MSI','HPE','NOK','LITE','ERIC','ZBRA','UI','ASTS','VIAV','VSAT','CIEN'] #Tech - Communication Equipment
J02 = ['ANET','DELL','HPQ','SMCI','WDC','PSTG','STX','SNDK','LOGI','IONQ'] #Tech - Computer Hardware
J03 = ['AAPL','SONY','LPL','SONO'] #Tech - Consumer Electronics
J04 = ['APH','TEL','GLW','CLS','JBL','FLEX','FN','TTMI','LFUS','SANM','VICR','OLED','PLXS','OSIS','RAL'] #Tech - Electronic Components
J05 = ['SNX','ARW','NSIT','AVT','CNXN','SCSC','CLMB'] #Tech - Electro & Compu Distribution
J06 = ['ACN','IBM','INFY','CTSH','FISV','FIS','WIT','LDOS','BR','CDW','GIB','CACI','JKHY','IT','EPAM','APLD','GDS','AUR','PSN','G'] #Tech - Info Techno Servs
J07 = ['COHR','KEYS','GRMN','TDY','FTV','MKSI','TRMB','CGNX','ESE','VNT','ST','NOVT','ITRI','BMI','ITRN'] #Tech - Scientific & Technical Instr
J08 = ['ASML','AMAT','LRCX','KLAC','TER','Q','ENTG','NVMI','ONTO','AMKR'] #Tech - Semiconductor Equip & Mats
J09 = ['NVDA','TSM','AVGO','MU','AMD','INTC','TXN','ADI','QCOM','ARM','MRVL','MPWR','NXPI','ASX','MCHP','ALAB','STM','ON','UMC','GFS'] #Tech - Semiconductors
J10 = ['CRM','SAP','UBER','SHOP','INTU','ADBE','NOW','ADP','CDNS','SNOW','ADSK','WDAY','DDOG','ROP','MSTR','PAYX','FICO','ZM','TEAM','PTC'] #Tech - Software - Application  (10/02/26: STRC not considered)
J11 = ['MSFT','ORCL','PLTR','PANW','CRWD','SNPS','FTNT','NET','CRWV','XYZ','MDB','ZS','CPAY','NBIS','VRSN','NTAP','GPN','CYBR','CHKP','TWLO'] #Tech - Software - Infraestructure
J12 = ['FSLR','ENPH','NXT','RUN','SEDG','ARRY','JKS','DQ','SHLS','CSIQ','TOYO'] #Tech - Solar
K01 = ['SRE','BIP','AES','AQN','CIG','AVA','UTL'] #Utilities - Diversified
K02 = ['CEG','VST','NRG','TLN','OKLO','PAM','TAC','KEN'] #Utilities - Independent Power Prods
K03 = ['NEE','SO','DUK','NGG','AEP','D','XEL','EXC','ETR','PEG','ED','WEC','PCG','AEE','DTE','KEP','FTS','FE','PPL','CNP'] #Utilities - Regulated Electric
K04 = ['ATO','NI','SWX','UGI','BIPC','NJR','BKH','SR','OGS','MDU','CPK','CTRI','NWN','SPH','OPAL'] #Utilities - Regulated Gas
K05 = ['AWK','WTRG','SBS','CWT','AWR','HTO','MSEX','CWCO'] #Utilities - Regulated Water
K06 = ['AXIA','BEP','ENLT','CWEN','CWEN-A','BEPC','ORA','FLNC','XIFR','RNW','NRGV'] #Utilities - Renewable

allindus = [A01,A02,A03,A04,A05,A06,A07,A08,A09,A10,A11,A12,A13,A14,
            B01,B02,B03,B04,B05,B06,B07,
            C01,C02,C03,C04,C05,C06,C07,C08,C09,C10,C11,C12,C13,C14,C15,C16,C17,C18,C19,C20,C21,C22,C23,
            D01,D02,D03,D04,D05,D06,D07,D08,D09,D10,D11,D12,
            E01,E02,E03,E04,E05,E06,E07,E08,
            F01,F02,F03,F04,F05,F06,F07,F08,F09,F10,F11,F12,F13,F14,F15,
            G01,G02,G03,G04,G05,G06,G07,G08,G09,G10,G11,
            H01,H02,H03,H04,H05,H06,H07,H08,H09,H10,H11,H12,H13,H14,H15,H16,H17,H18,H19,H20,H21,H22,H23,H24,H25,
            I01,I02,I03,I04,I05,I06,I07,I08,I09,I10,I11,I12,
            J01,J02,J03,J04,J05,J06,J07,J08,J09,J10,J11,J12,
            K01,K02,K03,K04,K05,K06]

#--------------------------------------------------

stock_indus = {'NTR':'(A01)', 'CTVA':'(A01)', 'CF': '(A01)', 'FMC': '(A01)', 'MOS': '(A01)', 'ICL': '(A01)', 'SMG': '(A01)', 'AA': '(A02)', 'CSTM': '(A02)', 'CENX': '(A02)', 'KALU': '(A02)', 'CRH': '(A03)', 'VMC': '(A03)', 'MLM': '(A03)', 'JHX': '(A03)', 'CX': '(A03)', 'EXP': '(A03)', 'SUM': '(A03)', 'BCC': '(A03)', 'KNF': '(A03)', 'TGLS': '(A03)', 'DOW': '(A04)', 'CE': '(A04)', 'HUN': '(A04)', 'BAK': '(A04)', 'MEOH': '(A04)', 'TROX': '(A04)', 'GPRE': '(A04)', 'AMR': '(A05)', 'ARCH': '(A05)', 'HCC': '(A05)', 'SXC': '(A05)', 'METC': '(A05)', 'SCCO': '(A06)', 'FCX': '(A06)', 'ERO': '(A06)', 'HBM': '(A06)', 'IE': '(A06)', 'NEM': '(A07)', 'AEM': '(A07)', 'GOLD': '(A07)', 'WPM': '(A07)', 'FNV': '(A07)', 'GFI': '(A07)', 'AU': '(A07)', 'KGC': '(A07)', 'RGLD': '(A07)', 'PAAS': '(A07)', 'AGI': '(A07)', 'HMY': '(A07)', 'BTG': '(A07)', 'EGO': '(A07)', 'OR': '(A07)', 'SSD': '(A08)', 'UFPI': '(A08)', 'WFG': '(A08)', 'NWGL': '(A08)', 'BHP': '(A09)', 'RIO': '(A09)', 'VALE': '(A09)', 'TECK': '(A09)', 'MP': '(A09)', 'MTRN': '(A09)', 'SGML': '(A09)', 'GSM': '(A09)', 'NEXA': '(A09)', 'TFPM': '(A10)', 'HL': '(A10)', 'BVN': '(A10)', 'SBSW': '(A10)', 'SILV': '(A10)', 'EXK': '(A10)', 'GATO': '(A10)', 'MUX': '(A10)', 'SLSR': '(A10)', 'PPTA': '(A10)', 'SUZ': '(A11)', 'SLVM': '(A11)', 'CLW': '(A11)', 'MERC': '(A11)', 'AG': '(A12)', 'MAG': '(A12)', 'SVM': '(A12)', 'LIN': '(A13)', 'SHW': '(A13)', 'ECL': '(A13)', 'APD': '(A13)', 'DD': '(A13)', 'LYB': '(A13)', 'PPG': '(A13)', 'IFF': '(A13)', 'WLK': '(A13)', 'AVTR': '(A13)', 'RPM': '(A13)', 'ALB': '(A13)', 'EMN': '(A13)', 'AXTA': '(A13)', 'SQM': '(A13)', 'OLN': '(A13)', 'ESI': '(A13)', 'CBT': '(A13)', 'NEU': '(A13)', 'ASH': '(A13)', 'NUE': '(A14)', 'MT': '(A14)', 'STLD': '(A14)', 'PKX': '(A14)', 'RS': '(A14)', 'X': '(A14)', 'TX': '(A14)', 'CLF': '(A14)', 'CMC': '(A14)', 'SIM': '(A14)', 'GGB': '(A14)', 'SID': '(A14)', 'WS': '(A14)', 'OMC': '(B01)', 'IPG': '(B01)', 'WPP': '(B01)', 'ZD': '(B01)', 'CMPR': '(B01)', 'CRTO': '(B01)', 'MGNI': '(B01)', 'IAS': '(B01)', 'EEX': '(B01)', 'DLX': '(B01)', 'TGNA': '(B02)', 'GTN': '(B02)', 'FUBO': '(B02)', 'SSP': '(B02)', 'IHRT': '(B02)', 'UONE': '(B02)', 'SGA': '(B02)', 'NTES': '(B03)', 'EA': '(B03)', 'RBLX': '(B03)', 'TTWO': '(B03)', 'BILI': '(B03)', 'PLTK': '(B03)', 'NFLX': '(B04)', 'DIS': '(B04)', 'LYV': '(B04)', 'WBD': '(B04)', 'FWONA': '(B04)', 'FOXA': '(B04)', 'FWONK': '(B04)', 'NWS': '(B04)', 'NWSA': '(B04)', 'WMG': '(B04)', 'FOX': '(B04)', 'SIRI': '(B04)', 'TKO': '(B04)', 'ROKU': '(B04)', 'EDR': '(B04)', 'PARA': '(B04)', 'LSXMA': '(B04)', 'LSXMK': '(B04)', 'GOOGL': '(B05)', 'GOOG': '(B05)', 'META': '(B05)', 'DASH': '(B05)', 'SPOT': '(B05)', 'PINS': '(B05)', 'BIDU': '(B05)', 'SNAP': '(B05)', 'RDDT': '(B05)', 'TME': '(B05)', 'MTCH': '(B05)', 'ZG': '(B05)', 'Z': '(B05)', 'TWLO': '(B05)', 'DJT': '(B05)', 'BZ': '(B05)', 'IAC': '(B05)', 'PSO': '(B06)', 'NYT': '(B06)', 'WLY': '(B06)', 'SCHL': '(B06)', 'GCI': '(B06)', 'CMCSA': '(B07)', 'TMUS': '(B07)', 'VZ': '(B07)', 'T': '(B07)', 'CHTR': '(B07)', 'AMX': '(B07)', 'BCE': '(B07)', 'ORAN': '(B07)', 'CHT': '(B07)', 'TEF': '(B07)', 'VOD': '(B07)', 'TLK': '(B07)', 'TU': '(B07)', 'RCI': '(B07)', 'VIV': '(B07)', 'RL': '(C01)', 'LEVI': '(C01)', 'PVH': '(C01)', 'GIL': '(C01)', 'VFC': '(C01)', 'COLM': '(C01)', 'KTB': '(C01)', 'UAA': '(C01)', 'ZGN': '(C01)', 'UA': '(C01)', 'HBI': '(C01)', 'OXM': '(C01)', 'GOOS': '(C01)', 'GIII': '(C01)', 'TJX': '(C02)', 'ROST': '(C02)', 'LULU': '(C02)', 'BURL': '(C02)', 'GPS': '(C02)', 'ANF': '(C02)', 'URBN': '(C02)', 'AEO': '(C02)', 'BOOT': '(C02)', 'CRI': '(C02)', 'FL': '(C02)', 'BKE': '(C02)', 'CVNA': '(C03)', 'KMX': '(C03)', 'PAG': '(C03)', 'LAD': '(C03)', 'AN': '(C03)', 'ABG': '(C03)', 'GPI': '(C03)', 'RUSHA': '(C03)', 'ACVA': '(C03)', 'CARG': '(C03)', 'SAH': '(C03)', 'TSLA': '(C04)', 'TM': '(C04)', 'VFS': '(C04)', 'HMC': '(C04)', 'RACE': '(C04)', 'STLA': '(C04)', 'F': '(C04)', 'GM': '(C04)', 'LI': '(C04)', 'NIO': '(C04)', 'RIVN': '(C04)', 'XPEV': '(C04)', 'LCID': '(C04)', 'APTV': '(C05)', 'MBLY': '(C05)', 'GPC': '(C05)', 'MGA': '(C05)', 'LKQ': '(C05)', 'ALV': '(C05)', 'BWA': '(C05)', 'GNTX': '(C05)', 'LEA': '(C05)', 'ALSN': '(C05)', 'MOD': '(C05)', 'GT': '(C05)', 'VC': '(C05)', 'QS': '(C05)', 'DDS': '(C06)', 'M': '(C06)', 'KSS': '(C06)', 'JWN': '(C06)', 'EXTO': '(C06)', 'NKE': '(C07)', 'DECK': '(C07)', 'ONON': '(C07)', 'SKX': '(C07)', 'BIRK': '(C07)', 'CROX': '(C07)', 'SHOO': '(C07)', 'SN': '(C08)', 'WHR': '(C08)', 'TPX': '(C08)', 'MHK': '(C08)', 'PATK': '(C08)', 'MBC': '(C08)', 'MLKN': '(C08)', 'LEG': '(C08)', 'LZB': '(C08)', 'AMWD': '(C08)', 'ETD': '(C08)', 'LOVE': '(C08)', 'FLUT': '(C09)', 'DKNG': '(C09)', 'CHDN': '(C09)', 'LNW': '(C09)', 'IGT': '(C09)', 'SGHC': '(C09)', 'ACEL': '(C09)', 'RSI': '(C09)', 'HD': '(C10)', 'LOW': '(C10)', 'FND': '(C10)', 'ARHS': '(C10)', 'AMZN': '(C11)', 'BABA': '(C11)', 'PDD': '(C11)', 'MELI': '(C11)', 'JD': '(C11)', 'CPNG': '(C11)', 'EBAY': '(C11)', 'SE': '(C11)', 'CHWY': '(C11)', 'CART': '(C11)', 'VIPS': '(C11)', 'ETSY': '(C11)', 'W': '(C11)', 'GLBE': '(C11)', 'HAS': '(C12)', 'AS': '(C12)', 'MAT': '(C12)', 'PLNT': '(C12)', 'YETI': '(C12)', 'GOLF': '(C12)', 'LTH': '(C12)', 'PRKS': '(C12)', 'MODG': '(C12)', 'SIX': '(C12)', 'FUN': '(C12)', 'VSTO': '(C12)', 'BOWL': '(C12)', 'MSGE': '(C12)', 'MAR': '(C13)', 'HLT': '(C13)', 'HTHT': '(C13)', 'IHG': '(C13)', 'H': '(C13)', 'CHH': '(C13)', 'WH': '(C13)', 'ATAT': '(C13)', 'TPR': '(C14)', 'CPRI': '(C14)', 'SIG': '(C14)', 'MOV': '(C14)', 'MYTE': '(C14)', 'REAL': '(C14)', 'LANV': '(C14)', 'BALL': '(C15)', 'AVY': '(C15)', 'AMCR': '(C15)', 'PKG': '(C15)', 'IP': '(C15)', 'CCK': '(C15)', 'WRK': '(C15)', 'GPK': '(C15)', 'BERY': '(C15)', 'SON': '(C15)', 'REYN': '(C15)', 'SEE': '(C15)', 'SLGN': '(C15)', 'GEF': '(C15)', 'ROL': '(C16)', 'SCI': '(C16)', 'HRB': '(C16)', 'BFAM': '(C16)', 'FTDR': '(C16)', 'MCW': '(C16)', 'CSV': '(C16)', 'PII': '(C17)', 'BC': '(C17)', 'THO': '(C17)', 'DOOO': '(C17)', 'HOG': '(C17)', 'LCII': '(C17)', 'WGO': '(C17)', 'MBUU': '(C17)', 'MPX': '(C17)', 'MCFT': '(C17)', 'DHI': '(C18)', 'LEN': '(C18)', 'NVR': '(C18)', 'PHM': '(C18)', 'TOL': '(C18)', 'TMHC': '(C18)', 'MTH': '(C18)', 'IBP': '(C18)', 'KBH': '(C18)', 'SKY': '(C18)', 'TPH': '(C18)', 'MHO': '(C18)', 'LVS': '(C19)', 'MGM': '(C19)', 'CZR': '(C19)', 'WYNN': '(C19)', 'MTN': '(C19)', 'BYD': '(C19)', 'MLCO': '(C19)', 'HGV': '(C19)', 'RRR': '(C19)', 'VAC': '(C19)', 'PENN': '(C19)', 'MCD': '(C20)', 'SBUX': '(C20)', 'CMG': '(C20)', 'YUM': '(C20)', 'YUMC': '(C20)', 'QSR': '(C20)', 'DRI': '(C20)', 'DPZ': '(C20)', 'TXRH': '(C20)', 'WING': '(C20)', 'CAVA': '(C20)', 'SG': '(C20)', 'SHAK': '(C20)', 'BROS': '(C20)', 'ORLY': '(C21)', 'AZO': '(C21)', 'TSCO': '(C21)', 'WSM': '(C21)', 'ULTA': '(C21)', 'DKS': '(C21)', 'BBY': '(C21)', 'CASY': '(C21)', 'BBWI': '(C21)', 'MUSA': '(C21)', 'FIVE': '(C21)', 'GME': '(C21)', 'MNSO': '(C21)', 'RH': '(C21)', 'ASO': '(C21)', 'AAP': '(C21)', 'AIN': '(C22)', 'UFI': '(C22)', 'CULP': '(C22)', 'BKNG': '(C23)', 'ABNB': '(C23)', 'TCOM': '(C23)', 'RCL': '(C23)', 'CCL': '(C23)', 'EXPE': '(C23)', 'VIK': '(C23)', 'MMYT': '(C23)', 'NCLH': '(C23)', 'TNL': '(C23)', 'BUD': '(D01)', 'ABEV': '(D01)', 'FMX': '(D01)', 'TAP': '(D01)', 'SAM': '(D01)', 'CCU': '(D01)', 'KO': '(D02)', 'PEP': '(D02)', 'MNST': '(D02)', 'KDP': '(D02)', 'CCEP': '(D02)', 'KOF': '(D02)', 'CELH': '(D02)', 'COKE': '(D02)', 'FIZZ': '(D02)', 'DEO': '(D03)', 'STZ': '(D03)', 'BF-A': '(D03)', 'BF-B': '(D03)', 'MGPI': '(D03)', 'MDLZ': '(D04)', 'HSY': '(D04)', 'TR': '(D04)', 'WMT': '(D05)', 'COST': '(D05)', 'TGT': '(D05)', 'DG': '(D05)', 'DLTR': '(D05)', 'BJ': '(D05)', 'OLLI': '(D05)', 'EDU': '(D06)', 'TAL': '(D06)', 'LOPE': '(D06)', 'GHC': '(D06)', 'LRN': '(D06)', 'STRA': '(D06)', 'ATGE': '(D06)', 'LAUR': '(D06)', 'PRDO': '(D06)', 'AFYA': '(D06)', 'UDMY': '(D06)', 'COUR': '(D06)', 'UTI': '(D06)', 'GOTU': '(D06)', 'ADM': '(D07)', 'TSN': '(D07)', 'BG': '(D07)', 'CALM': '(D07)', 'VITL': '(D07)', 'FDP': '(D07)', 'DOLE': '(D07)', 'AGRO': '(D07)', 'LND': '(D07)', 'SYY': '(D08)', 'USFD': '(D08)', 'PFGC': '(D08)', 'ANDE': '(D08)', 'CHEF': '(D08)', 'UNFI': '(D08)', 'AVO': '(D08)', 'SPTN': '(D08)', 'KR': '(D09)', 'ACI': '(D09)', 'SFM': '(D09)', 'ASAI': '(D09)', 'GO': '(D09)', 'DNUT': '(D09)', 'WMK': '(D09)', 'IMKTA': '(D09)', 'PG': '(D10)', 'UL': '(D10)', 'CL': '(D10)', 'EL': '(D10)', 'KVUE': '(D10)', 'KMB': '(D10)', 'CHD': '(D10)', 'CLX': '(D10)', 'ELF': '(D10)', 'COTY': '(D10)', 'HIMS': '(D10)', 'KHC': '(D11)', 'GIS': '(D11)', 'MKC': '(D11)', 'HRL': '(D11)', 'K': '(D11)', 'SJM': '(D11)', 'CAG': '(D11)', 'LW': '(D11)', 'CPB': '(D11)', 'PPC': '(D11)', 'BRBR': '(D11)', 'INGR': '(D11)', 'POST': '(D11)', 'FRPT': '(D11)', 'DAR': '(D11)', 'BRFS': '(D11)', 'LANC': '(D11)', 'FLO': '(D11)', 'SMPL': '(D11)', 'JJSF': '(D11)', 'PM': '(D12)', 'MO': '(D12)', 'BTI': '(D12)', 'NE': '(E01)', 'RIG': '(E01)', 'HP': '(E01)', 'SDRL': '(E01)', 'PTEN': '(E01)', 'BORR': '(E01)', 'DO': '(E01)', 'PDS': '(E01)', 'SOC': '(E01)', 'NBR': '(E01)', 'COP': '(E02)', 'CNQ': '(E02)', 'EOG': '(E02)', 'OXY': '(E02)', 'HES': '(E02)', 'FANG': '(E02)', 'WDS': '(E02)', 'DVN': '(E02)', 'CTRA': '(E02)', 'EQT': '(E02)', 'MRO': '(E02)', 'TPL': '(E02)', 'OVV': '(E02)', 'CHK': '(E02)', 'APA': '(E02)', 'AR': '(E02)', 'PR': '(E02)', 'RRC': '(E02)', 'SWN': '(E02)', 'MTDR': '(E02)', 'SLB': '(E03)', 'BKR': '(E03)', 'HAL': '(E03)', 'TS': '(E03)', 'FTI': '(E03)', 'WFRD': '(E03)', 'NOV': '(E03)', 'CHX': '(E03)', 'VAL': '(E03)', 'TDW': '(E03)', 'LBRT': '(E03)', 'WHD': '(E03)', 'AROC': '(E03)', 'USAC': '(E03)', 'AESI': '(E03)', 'XPRO': '(E03)', 'XOM': '(E04)', 'CVX': '(E04)', 'SHEL': '(E04)', 'TTE': '(E04)', 'BP': '(E04)', 'EQNR': '(E04)', 'PBR': '(E04)', 'SU': '(E04)', 'E': '(E04)', 'PBR-A': '(E04)', 'CVE': '(E04)', 'IMO': '(E04)', 'EC': '(E04)', 'YPF': '(E04)', 'NFG': '(E04)', 'ENB': '(E05)', 'EPD': '(E05)', 'WMB': '(E05)', 'ET': '(E05)', 'OKE': '(E05)', 'LNG': '(E05)', 'KMI': '(E05)', 'TRP': '(E05)', 'MPLX': '(E05)', 'CQP': '(E05)', 'TRGP': '(E05)', 'PBA': '(E05)', 'WES': '(E05)', 'PAA': '(E05)', 'AM': '(E05)', 'DTM': '(E05)', 'ETRN': '(E05)', 'ENLC': '(E05)', 'FRO': '(E05)', 'STNG': '(E05)', 'MPC': '(E06)', 'PSX': '(E06)', 'VLO': '(E06)', 'DINO': '(E06)', 'IEP': '(E06)', 'PBF': '(E06)', 'VVV': '(E06)', 'CSAN': '(E06)', 'UGP': '(E06)', 'SUN': '(E06)', 'CVI': '(E06)', 'ARLP': '(E07)', 'BTU': '(E07)', 'CEIX': '(E07)', 'NRP': '(E07)', 'HNRG': '(E07)', 'NC': '(E07)', 'CCJ': '(E08)', 'NXE': '(E08)', 'UEC': '(E08)', 'DNN': '(E08)', 'UUUU': '(E08)', 'EU': '(E08)', 'LEU': '(E08)', 'URG': '(E08)', 'UROY': '(E08)', 'BX': '(F01)', 'BLK': '(F01)', 'BN': '(F01)', 'KKR': '(F01)', 'APO': '(F01)', 'AMP': '(F01)', 'BK': '(F01)', 'ARES': '(F01)', 'TROW': '(F01)', 'STT': '(F01)', 'PFG': '(F01)', 'CRBG': '(F01)', 'NTRS': '(F01)', 'CG': '(F01)', 'ARCC': '(F01)', 'BEN': '(F01)', 'SEIC': '(F01)', 'OWL': '(F01)', 'BAM': '(F01)', 'JPM': '(F02)', 'BAC': '(F02)', 'WFC': '(F02)', 'HSBC': '(F02)', 'RY': '(F02)', 'TD': '(F02)', 'MUFG': '(F02)', 'UBS': '(F02)', 'C': '(F02)', 'SAN': '(F02)', 'SMFG': '(F02)', 'BMO': '(F02)', 'BNS': '(F02)', 'ING': '(F02)', 'BBVA': '(F02)', 'CM': '(F02)', 'BCS': '(F02)', 'HDB': '(F03)', 'IBN': '(F03)', 'PNC': '(F03)', 'USB': '(F03)', 'NU': '(F03)', 'MFG': '(F03)', 'TFC': '(F03)', 'LYG': '(F03)', 'NWG': '(F03)', 'DB': '(F03)', 'ITUB': '(F03)', 'FITB': '(F03)', 'FCNCA': '(F03)', 'MTB': '(F03)', 'KB': '(F03)', 'HBAN': '(F03)', 'BSBR': '(F03)', 'SHG': '(F03)', 'RF': '(F03)', 'CFG': '(F03)', 'MS': '(F04)', 'GS': '(F04)', 'SCHW': '(F04)', 'RJF': '(F04)', 'TW': '(F04)', 'LPLA': '(F04)', 'HOOD': '(F04)', 'NMR': '(F04)', 'IBKR': '(F04)', 'XP': '(F04)', 'MKTX': '(F04)', 'JEF': '(F04)', 'FUTU': '(F04)', 'HLI': '(F04)', 'SF': '(F04)', 'EVR': '(F04)', 'MARA': '(F04)', 'FRHC': '(F04)', 'V': '(F05)', 'MA': '(F05)', 'AXP': '(F05)', 'PYPL': '(F05)', 'COF': '(F05)', 'DFS': '(F05)', 'SYF': '(F05)', 'ALLY': '(F05)', 'SOFI': '(F05)', 'IX': '(F06)', 'VOYA': '(F06)', 'RILY': '(F06)', 'TREE': '(F06)', 'SPGI': '(F07)', 'CME': '(F07)', 'ICE': '(F07)', 'MCO': '(F07)', 'MSCI': '(F07)', 'NDAQ': '(F07)', 'COIN': '(F07)', 'FDS': '(F07)', 'CBOE': '(F07)', 'MORN': '(F07)', 'DNB': '(F07)', 'BRK-A': '(F08)', 'BRK-B': '(F08)', 'AIG': '(F08)', 'SLF': '(F08)', 'ACGL': '(F08)', 'AEG': '(F08)', 'EQH': '(F08)', 'MET': '(F09)', 'AFL': '(F09)', 'PUK': '(F09)', 'MFC': '(F09)', 'PRU': '(F09)', 'GL': '(F09)', 'UNM': '(F09)', 'PRI': '(F09)', 'JXN': '(F09)', 'LNC': '(F09)', 'FG': '(F09)', 'CNO': '(F09)', 'GNW': '(F09)', 'BHF': '(F09)', 'CB': '(F10)', 'PGR': '(F10)', 'TRV': '(F10)', 'ALL': '(F10)', 'MKL': '(F10)', 'HIG': '(F10)', 'CINF': '(F10)', 'WRB': '(F10)', 'L': '(F10)', 'CNA': '(F10)', 'AFG': '(F10)', 'KNSL': '(F10)', 'RLI': '(F10)', 'SIGI': '(F10)', 'THG': '(F10)', 'WTM': '(F10)', 'EG': '(F11)', 'RNR': '(F11)', 'RGA': '(F11)', 'BNRE': '(F11)', 'SPNT': '(F11)', 'HG': '(F11)', 'BNRE-A': '(F11)', 'RYAN': '(F12)', 'FNF': '(F12)', 'AIZ': '(F12)', 'AXS': '(F12)', 'FAF': '(F12)', 'ESNT': '(F12)', 'MTG': '(F12)', 'ACT': '(F12)', 'RDN': '(F12)', 'AGO': '(F12)', 'NMIH': '(F12)', 'TRUP': '(F12)', 'EIG': '(F12)', 'AMSF': '(F12)', 'TIPT': '(F12)', 'MMC': '(F13)', 'AON': '(F13)', 'AJG': '(F13)', 'WTW': '(F13)', 'BRO': '(F13)', 'ERIE': '(F13)', 'CRVL': '(F13)', 'BWIN': '(F13)', 'COOP': '(F14)', 'RKT': '(F14)', 'PFSI': '(F14)', 'WD': '(F14)', 'ECPG': '(F14)', 'GHLD': '(F14)', 'UWMC': '(F14)', 'VEL': '(F14)', 'LDI': '(F14)', 'GHI': '(F14)', 'OBDE': '(F15)', 'CVII': '(F15)', 'LPA': '(F15)', 'AACT': '(F15)', 'ANSC': '(F15)', 'NETD': '(F15)', 'GPATU': '(F15)', 'NVO': '(G01)', 'VRTX': '(G01)', 'REGN': '(G01)', 'MRNA': '(G01)', 'BNTX': '(G01)', 'ARGX': '(G01)', 'GMAB': '(G01)', 'ALNY': '(G01)', 'BGNE': '(G01)', 'RPRX': '(G01)', 'BMRN': '(G01)', 'INCY': '(G01)', 'TECH': '(G01)', 'LEGN': '(G01)', 'UTHR': '(G01)', 'SRPT': '(G01)', 'INSM': '(G01)', 'TMO': '(G02)', 'DHR': '(G02)', 'IDXX': '(G02)', 'IQV': '(G02)', 'A': '(G02)', 'ILMN': '(G02)', 'MTD': '(G02)', 'ICLR': '(G02)', 'LH': '(G02)', 'WAT': '(G02)', 'DGX': '(G02)', 'RVTY': '(G02)', 'NTRA': '(G02)', 'MEDP': '(G02)', 'CRL': '(G02)', 'QGEN': '(G02)', 'EXAS': '(G02)', 'LLY': '(G03)', 'JNJ': '(G03)', 'MRK': '(G03)', 'ABBV': '(G03)', 'NVS': '(G03)', 'AZN': '(G03)', 'PFE': '(G03)', 'AMGN': '(G03)', 'SNY': '(G03)', 'BMY': '(G03)', 'GILD': '(G03)', 'GSK': '(G03)', 'BIIB': '(G03)', 'ZTS': '(G04)', 'TAK': '(G04)', 'HLN': '(G04)', 'VTRS': '(G04)', 'RDY': '(G04)', 'TEVA': '(G04)', 'NBIX': '(G04)', 'CTLT': '(G04)', 'ELAN': '(G04)', 'ITCI': '(G04)', 'LNTH': '(G04)', 'ALVO': '(G04)', 'ALKS': '(G04)', 'PRGO': '(G04)', 'PBH': '(G04)', 'HCM': '(G04)', 'VEEV': '(G05)', 'SOLV': '(G05)', 'HQY': '(G05)', 'RCM': '(G05)', 'DOCS': '(G05)', 'GDRX': '(G05)', 'CERT': '(G05)', 'EVH': '(G05)', 'TXG': '(G05)', 'PGNY': '(G05)', 'PRVA': '(G05)', 'PINC': '(G05)', 'BTSG': '(G05)', 'TDOC': '(G05)', 'SDGR': '(G05)', 'OMCL': '(G05)', 'PHR': '(G05)', 'UNH': '(G06)', 'ELV': '(G06)', 'CVS': '(G06)', 'CI': '(G06)', 'HUM': '(G06)', 'CNC': '(G06)', 'MOH': '(G06)', 'HCA': '(G07)', 'THC': '(G07)', 'DVA': '(G07)', 'UHS': '(G07)', 'FMS': '(G07)', 'EHC': '(G07)', 'CHE': '(G07)', 'ENSG': '(G07)', 'ACHC': '(G07)', 'OPCH': '(G07)', 'PACS': '(G07)', 'SEM': '(G07)', 'SGRY': '(G07)', 'AMED': '(G07)', 'AGL': '(G07)', 'LFST': '(G07)', 'AMN': '(G07)', 'ABT': '(G08)', 'MDT': '(G08)', 'SYK': '(G08)', 'BSX': '(G08)', 'EW': '(G08)', 'DXCM': '(G08)', 'GEHC': '(G08)', 'ALGN': '(G08)', 'ZBH': '(G08)', 'STE': '(G08)', 'PHG': '(G08)', 'PODD': '(G08)', 'SWAV': '(G08)', 'SNN': '(G08)', 'BRKR': '(G08)', 'GMED': '(G08)', 'BIO': '(G08)', 'PEN': '(G08)', 'MASI': '(G08)', 'GKOS': '(G08)', 'MCK': '(G09)', 'COR': '(G09)', 'CAH': '(G09)', 'HSIC': '(G09)', 'PDCO': '(G09)', 'OMI': '(G09)', 'ISRG': '(G10)', 'BDX': '(G10)', 'ALC': '(G10)', 'WST': '(G10)', 'RMD': '(G10)', 'BAX': '(G10)', 'HOLX': '(G10)', 'COO': '(G10)', 'TFX': '(G10)', 'ATR': '(G10)', 'RGEN': '(G10)', 'XRAY': '(G10)', 'BLCO': '(G10)', 'STVN': '(G10)', 'WBA': '(G11)', 'HITI': '(G11)', 'PETS': '(G11)', 'GE': '(H01)', 'BA': '(H01)', 'RTX': '(H01)', 'LMT': '(H01)', 'GD': '(H01)', 'TDG': '(H01)', 'NOC': '(H01)', 'LHX': '(H01)', 'HWM': '(H01)', 'HEI': '(H01)', 'HEI-A': '(H01)', 'TXT': '(H01)', 'AXON': '(H01)', 'WWD': '(H01)', 'CW': '(H01)', 'HII': '(H01)', 'DAL': '(H02)', 'RYAAY': '(H02)', 'UAL': '(H02)', 'LUV': '(H02)', 'AAL': '(H02)', 'ALK': '(H02)', 'CPA': '(H02)', 'SKYW': '(H02)', 'JBLU': '(H02)', 'ULCC': '(H02)', 'ASR': '(H03)', 'PAC': '(H03)', 'JOBY': '(H03)', 'OMAB': '(H03)', 'CAAP': '(H03)', 'UP': '(H03)', 'ASLE': '(H03)', 'BLDE': '(H03)', 'TT': '(H04)', 'CARR': '(H04)', 'JCI': '(H04)', 'CSL': '(H04)', 'BLDR': '(H04)', 'LII': '(H04)', 'OC': '(H04)', 'MAS': '(H04)', 'WMS': '(H04)', 'TREX': '(H04)', 'FBIN': '(H04)', 'AZEK': '(H04)', 'LPX': '(H04)', 'SPXC': '(H04)', 'AAON': '(H04)', 'AWI': '(H04)', 'GMS': '(H04)', 'ASPN': '(H04)', 'HNI': '(H05)', 'SCS': '(H05)', 'EBF': '(H05)', 'ACTG': '(H05)', 'ACCO': '(H05)', 'HON': '(H06)', 'MMM': '(H06)', 'VMI': '(H06)', 'SEB': '(H06)', 'MDU': '(H06)', 'GFF': '(H06)', 'CODI': '(H06)', 'BBU': '(H06)', 'FBYD': '(H06)', 'VRSK': '(H07)', 'EFX': '(H07)', 'TRU': '(H07)', 'BAH': '(H07)', 'FCN': '(H07)', 'ICFI': '(H07)', 'HURN': '(H07)', 'CRAI': '(H07)', 'VRT': '(H08)', 'HUBB': '(H08)', 'NVT': '(H08)', 'AYI': '(H08)', 'ATKR': '(H08)', 'WIRE': '(H08)', 'ENS': '(H08)', 'AEIS': '(H08)', 'BE': '(H08)', 'HAYW': '(H08)', 'PLUG': '(H08)', 'ENR': '(H08)', 'POWL': '(H08)', 'ENVX': '(H08)', 'HOLI': '(H08)', 'PWR': '(H09)', 'EME': '(H09)', 'J': '(H09)', 'ACM': '(H09)', 'BLD': '(H09)', 'TTEK': '(H09)', 'FIX': '(H09)', 'STN': '(H09)', 'MTZ': '(H09)', 'KBR': '(H09)', 'FLR': '(H09)', 'APG': '(H09)', 'DY': '(H09)', 'EXPO': '(H09)', 'ACA': '(H09)', 'STRL': '(H09)', 'ROAD': '(H09)', 'PRIM': '(H09)', 'GVA': '(H09)', 'IESC': '(H09)', 'CAT': '(H10)', 'DE': '(H10)', 'PCAR': '(H10)', 'CNH': '(H10)', 'AGCO': '(H10)', 'OSK': '(H10)', 'TEX': '(H10)', 'ALG': '(H10)', 'REVG': '(H10)', 'GWW': '(H11)', 'FERG': '(H11)', 'FAST': '(H11)', 'WSO': '(H11)', 'POOL': '(H11)', 'CNM': '(H11)', 'WCC': '(H11)', 'AIT': '(H11)', 'BECN': '(H11)', 'SITE': '(H11)', 'MSM': '(H11)', 'UPS': '(H12)', 'FDX': '(H12)', 'ZTO': '(H12)', 'JBHT': '(H12)', 'EXPD': '(H12)', 'CHRW': '(H12)', 'GXO': '(H12)', 'LSTR': '(H12)', 'HUBG': '(H12)', 'KEX': '(H13)', 'HAFN': '(H13)', 'MATX': '(H13)', 'SBLK': '(H13)', 'BWLP': '(H13)', 'GOGL': '(H13)', 'ZIM': '(H13)', 'CDLR': '(H13)', 'SFL': '(H13)', 'CMRE': '(H13)', 'DAC': '(H13)', 'NMM': '(H13)', 'ECO': '(H13)', 'CPLP': '(H13)', 'GNK': '(H13)', 'ASC': '(H13)', 'NAT': '(H13)', 'SB': '(H13)', 'HSHP': '(H13)', 'PANL': '(H13)', 'ATI': '(H14)', 'MLI': '(H14)', 'ESAB': '(H14)', 'WOR': '(H14)', 'CRS': '(H14)', 'PRLB': '(H14)', 'RYI': '(H14)', 'HAYN': '(H14)', 'IIIN': '(H14)', 'VLTO': '(H15)', 'ZWS': '(H15)', 'FSS': '(H15)', 'ATMU': '(H15)', 'PCT': '(H15)', 'CECO': '(H15)', 'ERII': '(H15)', 'UNP': '(H16)', 'CP': '(H16)', 'CNI': '(H16)', 'CSX': '(H16)', 'NSC': '(H16)', 'WAB': '(H16)', 'URI': '(H17)', 'AER': '(H17)', 'UHAL': '(H17)', 'UHAL-B': '(H17)', 'FTAI': '(H17)', 'WSC': '(H17)', 'R': '(H17)', 'AL': '(H17)', 'GATX': '(H17)', 'CAR': '(H17)', 'HRI': '(H17)', 'MGRC': '(H17)', 'HEES': '(H17)', 'VSTS': '(H17)', 'PRG': '(H17)', 'CTOS': '(H17)', 'GSL': '(H17)', 'ALLE': '(H18)', 'MSA': '(H18)', 'ADT': '(H18)', 'BCO': '(H18)', 'BRC': '(H18)', 'REZI': '(H18)', 'GEO': '(H18)', 'NSSC': '(H18)', 'CXW': '(H18)', 'EVLV': '(H18)', 'NL': '(H18)', 'RELX': '(H19)', 'TRI': '(H19)', 'CTAS': '(H19)', 'CPRT': '(H19)', 'RTO': '(H19)', 'RBA': '(H19)', 'ARMK': '(H19)', 'ULS': '(H19)', 'DLB': '(H19)', 'MMS': '(H19)', 'CBZ': '(H19)', 'ABM': '(H19)', 'ETN': '(H20)', 'ITW': '(H20)', 'EMR': '(H20)', 'PH': '(H20)', 'AME': '(H20)', 'OTIS': '(H20)', 'ROK': '(H20)', 'CMI': '(H20)', 'IR': '(H20)', 'XYL': '(H20)', 'SYM': '(H20)', 'DOV': '(H20)', 'IEX': '(H20)', 'NDSN': '(H20)', 'GGG': '(H20)', 'PNR': '(H20)', 'AOS': '(H20)', 'ITT': '(H20)', 'RRX': '(H20)', 'DCI': '(H20)', 'GNRC': '(H20)', 'CR': '(H20)', 'ADP': '(H21)', 'PAYX': '(H21)', 'RHI': '(H21)', 'TNET': '(H21)', 'NSP': '(H21)', 'MAN': '(H21)', 'KFY': '(H21)', 'SNA': '(H22)', 'SWK': '(H22)', 'LECO': '(H22)', 'TTC': '(H22)', 'RBC': '(H22)', 'TKR': '(H22)', 'KMT': '(H22)', 'HLMN': '(H22)', 'ODFL': '(H23)', 'XPO': '(H23)', 'TFII': '(H23)', 'SAIA': '(H23)', 'KNX': '(H23)', 'SNDR': '(H23)', 'ARCB': '(H23)', 'RXO': '(H23)', 'WERN': '(H23)', 'MRTN': '(H23)', 'ULH': '(H23)', 'HTLD': '(H23)', 'WM': '(H24)', 'RSG': '(H24)', 'WCN': '(H24)', 'GFL': '(H24)', 'CLH': '(H24)', 'CWST': '(H24)', 'SRCL': '(H24)', 'FER': '(H25)', 'VRRM': '(H25)', 'VTMX': '(I01)', 'FOR': '(I01)', 'SDHC': '(I01)', 'LSEA': '(I01)', 'ARL': '(I01)', 'FPH': '(I01)', 'OZ': '(I01)', 'HHH': '(I02)', 'JOE': '(I02)', 'STRS': '(I02)', 'CSGP': '(I03)', 'CBRE': '(I03)', 'BEKE': '(I03)', 'FSV': '(I03)', 'JLL': '(I03)', 'CIGI': '(I03)', 'HASI': '(I03)', 'CWK': '(I03)', 'DBRG': '(I03)', 'COMP': '(I03)', 'EXPI': '(I03)', 'NMRK': '(I03)', 'OPEN': '(I03)', 'VICI': '(I04)', 'WPC': '(I04)', 'EPRT': '(I04)', 'BNL': '(I04)', 'GNL': '(I04)', 'ESRT': '(I04)', 'SAFE': '(I04)', 'AAT': '(I04)', 'AHH': '(I04)', 'WELL': '(I05)', 'VTR': '(I05)', 'DOC': '(I05)', 'OHI': '(I05)', 'HR': '(I05)', 'CTRE': '(I05)', 'SBRA': '(I05)', 'MPW': '(I05)', 'NHI': '(I05)', 'AHR': '(I05)', 'LTC': '(I05)', 'HST': '(I06)', 'RHP': '(I06)', 'APLE': '(I06)', 'PK': '(I06)', 'SHO': '(I06)', 'DRH': '(I06)', 'PEB': '(I06)', 'RLJ': '(I06)', 'XHR': '(I06)', 'SVC': '(I06)', 'INN': '(I06)', 'CLDT': '(I06)', 'PLD': '(I07)', 'PSA': '(I07)', 'EXR': '(I07)', 'REXR': '(I07)', 'CUBE': '(I07)', 'EGP': '(I07)', 'COLD': '(I07)', 'STAG': '(I07)', 'FR': '(I07)', 'TRNO': '(I07)', 'IIPR': '(I07)', 'NSA': '(I07)', 'LXP': '(I07)', 'NLY': '(I08)', 'STWD': '(I08)', 'AGNC': '(I08)', 'RITM': '(I08)', 'BXMT': '(I08)', 'ABR': '(I08)', 'ARI': '(I08)', 'RC': '(I08)', 'LADR': '(I08)', 'TWO': '(I08)', 'PMT': '(I08)', 'CMTG': '(I08)', 'MFA': '(I08)', 'FBRT': '(I08)', 'EFC': '(I08)', 'ARR': '(I08)', 'CIM': '(I08)', 'RWT': '(I08)', 'BRSP': '(I08)', 'DX': '(I08)', 'ARE': '(I09)', 'BXP': '(I09)', 'VNO': '(I09)', 'KRC': '(I09)', 'SLG': '(I09)', 'CUZ': '(I09)', 'CDP': '(I09)', 'HIW': '(I09)', 'DEI': '(I09)', 'EQC': '(I09)', 'ESBA': '(I09)', 'JBGS': '(I09)', 'DEA': '(I09)', 'PGRE': '(I09)', 'PDM': '(I09)', 'BDN': '(I09)', 'HPP': '(I09)', 'AVB': '(I10)', 'EQR': '(I10)', 'INVH': '(I10)', 'MAA': '(I10)', 'SUI': '(I10)', 'ESS': '(I10)', 'UDR': '(I10)', 'AMH': '(I10)', 'ELS': '(I10)', 'CPT': '(I10)', 'AIRC': '(I10)', 'IRT': '(I10)', 'O': '(I11)', 'SPG': '(I11)', 'KIM': '(I11)', 'REG': '(I11)', 'FRT': '(I11)', 'NNN': '(I11)', 'BRX': '(I11)', 'ADC': '(I11)', 'KRG': '(I11)', 'PECO': '(I11)', 'MAC': '(I11)', 'SITC': '(I11)', 'SKT': '(I11)', 'FCPT': '(I11)', 'UE': '(I11)', 'AKR': '(I11)', 'AMT': '(I12)', 'EQIX': '(I12)', 'CCI': '(I12)', 'DLR': '(I12)', 'WY': '(I12)', 'SBAC': '(I12)', 'IRM': '(I12)', 'GLPI': '(I12)', 'LAMR': '(I12)', 'RYN': '(I12)', 'PCH': '(I12)', 'EPR': '(I12)', 'CSCO': '(J01)', 'MSI': '(J01)', 'HPE': '(J01)', 'NOK': '(J01)', 'ERIC': '(J01)', 'ZBRA': '(J01)', 'JNPR': '(J01)', 'UI': '(J01)', 'CIEN': '(J01)', 'SATS': '(J01)', 'PI': '(J01)', 'BDC': '(J01)', 'ANET': '(J02)', 'DELL': '(J02)', 'HPQ': '(J02)', 'NTAP': '(J02)', 'SMCI': '(J02)', 'WDC': '(J02)', 'PSTG': '(J02)', 'STX': '(J02)', 'LOGI': '(J02)', 'AAPL': '(J03)', 'SONY': '(J03)', 'LPL': '(J03)', 'VZIO': '(J03)', 'APH': '(J04)', 'TEL': '(J04)', 'GLW': '(J04)', 'JBL': '(J04)', 'FLEX': '(J04)', 'OLED': '(J04)', 'FN': '(J04)', 'CLS': '(J04)', 'LFUS': '(J04)', 'SANM': '(J04)', 'PLXS': '(J04)', 'OSIS': '(J04)', 'ROG': '(J04)', 'SNX': '(J05)', 'ARW': '(J05)', 'NSIT': '(J05)', 'AVT': '(J05)', 'CNXN': '(J05)', 'SCSC': '(J05)', 'SNPO': '(J05)', 'CLMB': '(J05)', 'ACN': '(J06)', 'IBM': '(J06)', 'FI': '(J06)', 'INFY': '(J06)', 'FIS': '(J06)', 'CTSH': '(J06)', 'CDW': '(J06)', 'WIT': '(J06)', 'IT': '(J06)', 'BR': '(J06)', 'GIB': '(J06)', 'LDOS': '(J06)', 'JKHY': '(J06)', 'EPAM': '(J06)', 'CACI': '(J06)', 'GRMN': '(J07)', 'FTV': '(J07)', 'KEYS': '(J07)', 'TDY': '(J07)', 'TRMB': '(J07)', 'COHR': '(J07)', 'MKSI': '(J07)', 'CGNX': '(J07)', 'VNT': '(J07)', 'ST': '(J07)', 'NOVT': '(J07)', 'BMI': '(J07)', 'ITRI': '(J07)', 'ESE': '(J07)', 'ASML': '(J08)', 'AMAT': '(J08)', 'LRCX': '(J08)', 'KLAC': '(J08)', 'TER': '(J08)', 'ENTG': '(J08)', 'ONTO': '(J08)', 'AMKR': '(J08)', 'NVDA': '(J09)', 'TSM': '(J09)', 'AVGO': '(J09)', 'AMD': '(J09)', 'QCOM': '(J09)', 'TXN': '(J09)', 'MU': '(J09)', 'INTC': '(J09)', 'ARM': '(J09)', 'ADI': '(J09)', 'NXPI': '(J09)', 'MRVL': '(J09)', 'MCHP': '(J09)', 'STM': '(J09)', 'MPWR': '(J09)', 'ON': '(J09)', 'GFS': '(J09)', 'ASX': '(J09)', 'UMC': '(J09)', 'SWKS': '(J09)', 'LSCC': '(J09)', 'CRM': '(J10)', 'SAP': '(J10)', 'INTU': '(J10)', 'NOW': '(J10)', 'UBER': '(J10)', 'SHOP': '(J10)', 'CDNS': '(J10)', 'WDAY': '(J10)', 'ROP': '(J10)', 'SNOW': '(J10)', 'TEAM': '(J10)', 'ADSK': '(J10)', 'TTD': '(J10)', 'DDOG': '(J10)', 'ANSS': '(J10)', 'HUBS': '(J10)', 'MSTR': '(J10)', 'APP': '(J10)', 'FICO': '(J10)', 'ZM': '(J10)', 'TYL': '(J10)', 'PTC': '(J10)', 'MSFT': '(J11)', 'ORCL': '(J11)', 'ADBE': '(J11)', 'PANW': '(J11)', 'SNPS': '(J11)', 'FTNT': '(J11)', 'CRWD': '(J11)', 'SQ': '(J11)', 'PLTR': '(J11)', 'MDB': '(J11)', 'VRSN': '(J11)', 'ZS': '(J11)', 'GPN': '(J11)', 'NET': '(J11)', 'FLT': '(J11)', 'CHKP': '(J11)', 'AKAM': '(J11)', 'GEN': '(J11)', 'IOT': '(J11)', 'FSLR': '(J12)', 'ENPH': '(J12)', 'NXT': '(J12)', 'RUN': '(J12)', 'SEDG': '(J12)', 'ARRY': '(J12)', 'JKS': '(J12)', 'DQ': '(J12)', 'SHLS': '(J12)', 'CSIQ': '(J12)', 'NOVA': '(J12)', 'SRE': '(K01)', 'BIP': '(K01)', 'AES': '(K01)', 'OTTR': '(K01)', 'ALE': '(K01)', 'CIG': '(K01)', 'AVA': '(K01)', 'ELPC': '(K01)', 'VST': '(K02)', 'NRG': '(K02)', 'PAM': '(K02)', 'TAC': '(K02)', 'KEN': '(K02)', 'NEE': '(K03)', 'SO': '(K03)', 'DUK': '(K03)', 'NGG': '(K03)', 'AEP': '(K03)', 'PCG': '(K03)', 'D': '(K03)', 'PEG': '(K03)', 'EXC': '(K03)', 'ED': '(K03)', 'XEL': '(K03)', 'EIX': '(K03)', 'WEC': '(K03)', 'DTE': '(K03)', 'ETR': '(K03)', 'FE': '(K03)', 'PPL': '(K03)', 'ES': '(K03)', 'FTS': '(K03)', 'CNP': '(K03)', 'AEE': '(K03)', 'CMS': '(K03)', 'AGR': '(K03)', 'LNT': '(K03)', 'EVRG': '(K03)', 'ATO': '(K04)', 'NI': '(K04)', 'SWX': '(K04)', 'UGI': '(K04)', 'BIPC': '(K04)', 'NFE': '(K04)', 'NJR': '(K04)', 'BKH': '(K04)', 'SR': '(K04)', 'OGS': '(K04)', 'CPK': '(K04)', 'CTRI': '(K04)', 'NWN': '(K04)', 'SPH': '(K04)', 'AWK': '(K05)', 'WTRG': '(K05)', 'SBS': '(K05)', 'CWT': '(K05)', 'AWR': '(K05)', 'SJW': '(K05)', 'MSEX': '(K05)', 'YORW': '(K05)', 'CEG': '(K06)', 'GEV': '(K06)', 'EBR': '(K06)', 'BEPC': '(K06)', 'BEP': '(K06)', 'ORA': '(K06)', 'AQN': '(K06)', 'CWEN': '(K06)', 'NEP': '(K06)', 'CWEN-A': '(K06)', 'FLNC': '(K06)', 'AY': '(K06)', 'RNW': '(K06)', 'ENLT': '(K06)'}

#--------------------------------------------------
all_comps = []
for gro in allindus:
    for sto in gro:
        all_comps.append(sto)
#--------------------------------------------------
def indus_names(gr):
    if gr == A01:
        gro_des = 'A01 Basic Materials - Agricultural inputs'
    elif gr == A02:
        gro_des = 'A02 Basic Materials - Aluminum'
    elif gr == A03:
        gro_des = 'A03 Basic Materials - Building materials'
    elif gr == A04:
        gro_des = 'A04 Basic Materials - Chemicals'
    elif gr == A05:
        gro_des = 'A05 Basic Materials - Coking coal'
    elif gr == A06:
        gro_des = 'A06 Basic Materials - Copper'
    elif gr == A07:
        gro_des = 'A07 Basic Materials - Gold'
    elif gr == A08:
        gro_des = 'A08 Basic Materials - Lumber & Wood production'
    elif gr == A09:
        gro_des = 'A09 Basic Materials - Other Industrial Metals & Mining'
    elif gr == A10:
        gro_des = 'A10 Basic Materials - Other Precious Metals & Mining'
    elif gr == A11:
        gro_des = 'A11 Basic Materials - Paper & Paper products'
    elif gr == A12:
        gro_des = 'A12 Basic Materials - Silver'
    elif gr == A13:
        gro_des = 'A13 Basic Materials - Specialty Chemicals'
    elif gr == A14:
        gro_des = 'A14 Basic Materials - Steel'
    elif gr == B01:
        gro_des = 'B01 Communication Services - Advertising Agencies'
    elif gr == B02:
        gro_des = 'B02 Communication Services - Broadcasting'
    elif gr == B03:
        gro_des = 'B03 Communication Services - Electronic Gaming & Multimedia'
    elif gr == B04:
        gro_des = 'B04 Communication Services - Entertainment'
    elif gr == B05:
        gro_des = 'B05 Communication Services - Internet Content & Information'
    elif gr == B06:
        gro_des = 'B06 Communication Services - Publishing'
    elif gr == B07:
        gro_des = 'B07 Communication Services - Telecom Services'
    elif gr == C01:
        gro_des = 'C01 Consumer Cyclical - Apparel Manufacturing'
    elif gr == C02:
        gro_des = 'C02 Consumer Cyclical - Apparel Retail'
    elif gr == C03:
        gro_des = 'C03 Consumer Cyclical - Auto & Truck Dealerships'
    elif gr == C04:
        gro_des = 'C04 Consumer Cyclical - Auto Manufacturers'
    elif gr == C05:
        gro_des = 'C05 Consumer Cyclical - Auto Parts'
    elif gr == C06:
        gro_des = 'C06 Consumer Cyclical - Department Stores'
    elif gr == C07:
        gro_des = 'C07 Consumer Cyclical - Footwear & Accesories'
    elif gr == C08:
        gro_des = 'C08 Consumer Cyclical - Furnishings, Fixtures and Appliances'
    elif gr == C09:
        gro_des = 'C09 Consumer Cyclical - Gambling'
    elif gr == C10:
        gro_des = 'C10 Consumer Cyclical - Home Improvement Retail'
    elif gr == C11:
        gro_des = 'C11 Consumer Cyclical - Internet Retail'
    elif gr == C12:
        gro_des = 'C12 Consumer Cyclical - Leisure'
    elif gr == C13:
        gro_des = 'C13 Consumer Cyclical - Lodging'
    elif gr == C14:
        gro_des = 'C14 Consumer Cyclical - Luxury Goods'
    elif gr == C15:
        gro_des = 'C15 Consumer Cyclical - Packaging & Containers'
    elif gr == C16:
        gro_des = 'C16 Consumer Cyclical - Personal Services'
    elif gr == C17:
        gro_des = 'C17 Consumer Cyclical - Recreational Vehicles'
    elif gr == C18:
        gro_des = 'C18 Consumer Cyclical - Residential Construction'
    elif gr == C19:
        gro_des = 'C19 Consumer Cyclical - Resorts & Casinos'
    elif gr == C20:
        gro_des = 'C20 Consumer Cyclical - Restaurants'
    elif gr == C21:
        gro_des = 'C21 Consumer Cyclical - Specialty Retail'
    elif gr == C22:
        gro_des = 'C22 Consumer Cyclical - Textile Manufacturing'
    elif gr == C23:
        gro_des = 'C23 Consumer Cyclical - Travel services'
    elif gr == D01:
        gro_des = 'D01 Consumer Defensive - Beverages - Brewers'
    elif gr == D02:
        gro_des = 'D02 Consumer Defensive - Beverages - Non Alcoholic'
    elif gr == D03:
        gro_des = 'D03 Consumer Defensive - Beverages - Wineries & Distilleries'
    elif gr == D04:
        gro_des = 'D04 Consumer Defensive - Confectioners'
    elif gr == D05:
        gro_des = 'D05 Consumer Defensive - Discount Stores'
    elif gr == D06:
        gro_des = 'D06 Consumer Defensive - Education & Training Services'
    elif gr == D07:
        gro_des = 'D07 Consumer Defensive - Farm products'
    elif gr == D08:
        gro_des = 'D08 Consumer Defensive - Food Distribution'
    elif gr == D09:
        gro_des = 'D09 Consumer Defensive - Grocery Stores'
    elif gr == D10:
        gro_des = 'D10 Consumer Defensive - Household & Personal products'
    elif gr == D11:
        gro_des = 'D11 Consumer Defensive - Packaged Foods'
    elif gr == D12:
        gro_des = 'D12 Consumer Defensive - Tobacco'
    elif gr == E01:
        gro_des = 'E01 Energy - Oil & Gas Drilling'
    elif gr == E02:
        gro_des = 'E02 Energy - Oil & Gas E&P'
    elif gr == E03:
        gro_des = 'E03 Energy - Oil & Gas Equipment & Services'
    elif gr == E04:
        gro_des = 'E04 Energy - Oil & Gas Integrated'
    elif gr == E05:
        gro_des = 'E05 Energy - Oil & Gas Midstream'
    elif gr == E06:
        gro_des = 'E06 Energy - Oil & Gas Refining & Marketing'
    elif gr == E07:
        gro_des = 'E07 Energy - Thermal coal'
    elif gr == E08:
        gro_des = 'E08 Energy - Uranium'
    elif gr == F01:
        gro_des = 'F01 Financial - Asset Management'
    elif gr == F02:
        gro_des = 'F02 Financial - Banks - Diversified'
    elif gr == F03:
        gro_des = 'F03 Financial - Banks - Regional'
    elif gr == F04:
        gro_des = 'F04 Financial - Capital Markets'
    elif gr == F05:
        gro_des = 'F05 Financial - Credit Services'
    elif gr == F06:
        gro_des = 'F06 Financial - Financial Conglomerates'
    elif gr == F07:
        gro_des = 'F07 Financial - Financial Data & Stock Exchanges'
    elif gr == F08:
        gro_des = 'F08 Financial - Insurance - Diversified'
    elif gr == F09:
        gro_des = 'F09 Financial - Insurance - Life'
    elif gr == F10:
        gro_des = 'F10 Financial - Insurance - Property & Casualty'
    elif gr == F11:
        gro_des = 'F11 Financial - Insurance - Reinsurance'
    elif gr == F12:
        gro_des = 'F12 Financial - Insurance - Specialty'
    elif gr == F13:
        gro_des = 'F13 Financial - Insurance Brokers'
    elif gr == F14:
        gro_des = 'F14 Financial - Mortgage finance'
    elif gr == F15:
        gro_des = 'F15 Financial - Shell Companies'
    elif gr == G01:
        gro_des = 'G01 Healthcare - Biotechnology'
    elif gr == G02:
        gro_des = 'G02 Healthcare - Diagnostics & Research'
    elif gr == G03:
        gro_des = 'G03 Healthcare - Drug Manufacturers - General'
    elif gr == G04:
        gro_des = 'G04 Healthcare - Drug Manufacturers - Specialty & Generic'
    elif gr == G05:
        gro_des = 'G05 Healthcare - Health Information Services'
    elif gr == G06:
        gro_des = 'G06 Healthcare - Healthcare plans'
    elif gr == G07:
        gro_des = 'G07 Healthcare - Medical Care Facilities'
    elif gr == G08:
        gro_des = 'G08 Healthcare - Medical Devices'
    elif gr == G09:
        gro_des = 'G09 Healthcare - Medical Distribution'
    elif gr == G10:
        gro_des = 'G10 Healthcare - Medical Instruments & Supplies'
    elif gr == G11:
        gro_des = 'G11 Healthcare - Pharmaceutical Retailers'
    elif gr == H01:
        gro_des = 'H01 Industrials - Aerospace & Defense'
    elif gr == H02:
        gro_des = 'H02 Industrials - Airlines'
    elif gr == H03:
        gro_des = 'H03 Industrials - Airports & Air Services'
    elif gr == H04:
        gro_des = 'H04 Industrials - Building Products & Equipment'
    elif gr == H05:
        gro_des = 'H05 Industrials - Business Equipment & Supplies'
    elif gr == H06:
        gro_des = 'H06 Industrials - Conglomerates'
    elif gr == H07:
        gro_des = 'H07 Industrials - Consulting Services'
    elif gr == H08:
        gro_des = 'H08 Industrials - Electrical Equipment & parts'
    elif gr == H09:
        gro_des = 'H09 Industrials - Engineering & Construction'
    elif gr == H10:
        gro_des = 'H10 Industrials - Farm & Heavy Construction Machinery'
    elif gr == H11:
        gro_des = 'H11 Industrials - Industrial Distribution'
    elif gr == H12:
        gro_des = 'H12 Industrials - Integrated Freight & Logistics'
    elif gr == H13:
        gro_des = 'H13 Industrials - Marine Shipping'
    elif gr == H14:
        gro_des = 'H14 Industrials - Metal Fabrication'
    elif gr == H15:
        gro_des = 'H15 Industrials - Pollution & Treatment Controls'
    elif gr == H16:
        gro_des = 'H16 Industrials - Railroads'
    elif gr == H17:
        gro_des = 'H17 Industrials - Rental & Leasing Services'
    elif gr == H18:
        gro_des = 'H18 Industrials - Security & Protection Services'
    elif gr == H19:
        gro_des = 'H19 Industrials - Specialty Business Services'
    elif gr == H20:
        gro_des = 'H20 Industrials - Specialty Industrial Machinery'
    elif gr == H21:
        gro_des = 'H21 Industrials - Staffing & Employment Services'
    elif gr == H22:
        gro_des = 'H22 Industrials - Tools & Accessories'
    elif gr == H23:
        gro_des = 'H23 Industrials - Trucking'
    elif gr == H24:
        gro_des = 'H24 Industrials - Waste Management'
    elif gr == H25:
        gro_des = 'H25 Industrials - Infrastructure Operations'
    elif gr == I01:
        gro_des = 'I01 Real Estate - Real Estate  Development'
    elif gr == I02:
        gro_des = 'I02 Real Estate - Real Estate  Diversified'
    elif gr == I03:
        gro_des = 'I03 Real Estate - Real Estate  Services'
    elif gr == I04:
        gro_des = 'I04 Real Estate - REIT - Diversified'
    elif gr == I05:
        gro_des = 'I05 Real Estate - REIT - Healthcare Facilities'
    elif gr == I06:
        gro_des = 'I06 Real Estate - REIT - Hotel & Motel'
    elif gr == I07:
        gro_des = 'I07 Real Estate - REIT - Industrial'
    elif gr == I08:
        gro_des = 'I08 Real Estate - REIT - Mortgage'
    elif gr == I09:
        gro_des = 'I09 Real Estate - REIT - Office'
    elif gr == I10:
        gro_des = 'I10 Real Estate - REIT - Residential'
    elif gr == I11:
        gro_des = 'I11 Real Estate - REIT - Retail'
    elif gr == I12:
        gro_des = 'I12 Real Estate - REIT - Specialty'
    elif gr == J01:
        gro_des = 'J01 Technology - Communication Equipment'
    elif gr == J02:
        gro_des = 'J02 Technology - Computer Hardware'
    elif gr == J03:
        gro_des = 'J03 Technology - Consumer Electronics'
    elif gr == J04:
        gro_des = 'J04 Technology - Electronic Components'
    elif gr == J05:
        gro_des = 'J05 Technology - Electronics & Computer Distribution'
    elif gr == J06:
        gro_des = 'J06 Technology - Information Technology Services'
    elif gr == J07:
        gro_des = 'J07 Technology - Scientific & Technical Instruments'
    elif gr == J08:
        gro_des = 'J08 Technology - Semiconductor Equipment & Materials'
    elif gr == J09:
        gro_des = 'J09 Technology - Semiconductors'
    elif gr == J10:
        gro_des = 'J10 Technology - Software - Application'
    elif gr == J11:
        gro_des = 'J11 Technology - Software - Infraestructure'
    elif gr == J12:
        gro_des = 'J12 Technology - Solar'
    elif gr == K01:
        gro_des = 'K01 Utilities - Diversified'
    elif gr == K02:
        gro_des = 'K02 Utilities - Independent Power Producers'
    elif gr == K03:
        gro_des = 'K03 Utilities - Regulated Electric'
    elif gr == K04:
        gro_des = 'K04 Utilities - Regulated Gas'
    elif gr == K05:
        gro_des = 'K05 Utilities - Regulated Water'
    elif gr == K06:
        gro_des = 'K06 Utilities - Renewable'
    else:
        gro_des = gro
    return gro_des        
#--------------------------------------------------


#=========================================================================================

lis_sectors = ['Basic Materials','Communication Services','Consumer Cyclical','Consumer Defensive','Energy','Financial','Healthcare','Industrials','Real Estate','Technology','Utilities']
opts_lis_sectors = ['*Select all sectors','Basic Materials','Communication Services','Consumer Cyclical','Consumer Defensive','Energy','Financial','Healthcare','Industrials','Real Estate','Technology','Utilities']
opts_industries = ['*Select all industries', 'Basic Materials - Agricultural inputs', 'Basic Materials - Aluminum', 'Basic Materials - Building materials', 'Basic Materials - Chemicals', 'Basic Materials - Coking coal', 'Basic Materials - Copper', 'Basic Materials - Gold', 'Basic Materials - Lumber & Wood production', 'Basic Materials - Other Industrial Metals & Mining', 'Basic Materials - Other Precious Metals & Mining', 'Basic Materials - Paper & Paper products', 'Basic Materials - Silver', 'Basic Materials - Specialty Chemicals', 'Basic Materials - Steel', 'Communication Services - Advertising Agencies', 'Communication Services - Broadcasting', 'Communication Services - Electronic Gaming & Multimedia', 'Communication Services - Entertainment', 'Communication Services - Internet Content & Information', 'Communication Services - Publishing', 'Communication Services - Telecom Services', 'Consumer Cyclical - Apparel Manufacturing', 'Consumer Cyclical - Apparel Retail', 'Consumer Cyclical - Auto & Truck Dealerships', 'Consumer Cyclical - Auto Manufacturers', 'Consumer Cyclical - Auto Parts', 'Consumer Cyclical - Department Stores', 'Consumer Cyclical - Footwear & Accesories', 'Consumer Cyclical - Furnishings, Fixtures and Appliances', 'Consumer Cyclical - Gambling', 'Consumer Cyclical - Home Improvement Retail', 'Consumer Cyclical - Internet Retail', 'Consumer Cyclical - Leisure', 'Consumer Cyclical - Lodging', 'Consumer Cyclical - Luxury Goods', 'Consumer Cyclical - Packaging & Containers', 'Consumer Cyclical - Personal Services', 'Consumer Cyclical - Recreational Vehicles', 'Consumer Cyclical - Residential Construction', 'Consumer Cyclical - Resorts & Casinos', 'Consumer Cyclical - Restaurants', 'Consumer Cyclical - Specialty Retail', 'Consumer Cyclical - Textile Manufacturing', 'Consumer Cyclical - Travel services', 'Consumer Defensive - Beverages - Brewers', 'Consumer Defensive - Beverages - Non Alcoholic', 'Consumer Defensive - Beverages - Wineries & Distilleries', 'Consumer Defensive - Confectioners', 'Consumer Defensive - Discount Stores', 'Consumer Defensive - Education & Training Services', 'Consumer Defensive - Farm products', 'Consumer Defensive - Food Distribution', 'Consumer Defensive - Grocery Stores', 'Consumer Defensive - Household & Personal products', 'Consumer Defensive - Packaged Foods', 'Consumer Defensive - Tobacco', 'Energy - Oil & Gas Drilling', 'Energy - Oil & Gas E&P', 'Energy - Oil & Gas Equipment & Services', 'Energy - Oil & Gas Integrated', 'Energy - Oil & Gas Midstream', 'Energy - Oil & Gas Refining & Marketing', 'Energy - Thermal coal', 'Energy - Uranium', 'Financial - Asset Management', 'Financial - Banks - Diversified', 'Financial - Banks - Regional', 'Financial - Capital Markets', 'Financial - Credit Services', 'Financial - Financial Conglomerates', 'Financial - Financial Data & Stock Exchanges', 'Financial - Insurance - Diversified', 'Financial - Insurance - Life', 'Financial - Insurance - Property & Casualty', 'Financial - Insurance - Reinsurance', 'Financial - Insurance - Specialty', 'Financial - Insurance Brokers', 'Financial - Mortgage finance', 'Financial - Shell Companies', 'Healthcare - Biotechnology', 'Healthcare - Diagnostics & Research', 'Healthcare - Drug Manufacturers - General', 'Healthcare - Drug Manufacturers - Specialty & Generic', 'Healthcare - Health Information Services', 'Healthcare - Healthcare plans', 'Healthcare - Medical Care Facilities', 'Healthcare - Medical Devices', 'Healthcare - Medical Distribution', 'Healthcare - Medical Instruments & Supplies', 'Healthcare - Pharmaceutical Retailers', 'Industrials - Aerospace & Defense', 'Industrials - Airlines', 'Industrials - Airports & Air Services', 'Industrials - Building Products & Equipment', 'Industrials - Business Equipment & Supplies', 'Industrials - Conglomerates', 'Industrials - Consulting Services', 'Industrials - Electrical Equipment & parts', 'Industrials - Engineering & Construction', 'Industrials - Farm & Heavy Construction Machinery', 'Industrials - Industrial Distribution', 'Industrials - Integrated Freight & Logistics', 'Industrials - Marine Shipping', 'Industrials - Metal Fabrication', 'Industrials - Pollution & Treatment Controls', 'Industrials - Railroads', 'Industrials - Rental & Leasing Services', 'Industrials - Security & Protection Services', 'Industrials - Specialty Business Services', 'Industrials - Specialty Industrial Machinery', 'Industrials - Staffing & Employment Services', 'Industrials - Tools & Accessories', 'Industrials - Trucking', 'Industrials - Waste Management', 'Industrials - Infrastructure Operations', 'Real Estate - Real Estate  Development', 'Real Estate - Real Estate  Diversified', 'Real Estate - Real Estate  Services', 'Real Estate - REIT - Diversified', 'Real Estate - REIT - Healthcare Facilities', 'Real Estate - REIT - Hotel & Motel', 'Real Estate - REIT - Industrial', 'Real Estate - REIT - Mortgage', 'Real Estate - REIT - Office', 'Real Estate - REIT - Residential', 'Real Estate - REIT - Retail', 'Real Estate - REIT - Specialty', 'Technology - Communication Equipment', 'Technology - Computer Hardware', 'Technology - Consumer Electronics', 'Technology - Electronic Components', 'Technology - Electronics & Computer Distribution', 'Technology - Information Technology Services', 'Technology - Scientific & Technical Instruments', 'Technology - Semiconductor Equipment & Materials', 'Technology - Semiconductors', 'Technology - Software - Application', 'Technology - Software - Infraestructure', 'Technology - Solar', 'Utilities - Diversified', 'Utilities - Independent Power Producers', 'Utilities - Regulated Electric', 'Utilities - Regulated Gas', 'Utilities - Regulated Water', 'Utilities - Renewable']

indu = [('A01','Basic Materials - Agricultural inputs'),
('A02','Basic Materials - Aluminum'),
('A03','Basic Materials - Building materials'),
('A04','Basic Materials - Chemicals'),
('A05','Basic Materials - Coking coal'),
('A06','Basic Materials - Copper'),
('A07','Basic Materials - Gold'),
('A08','Basic Materials - Lumber & Wood production'),
('A09','Basic Materials - Other Industrial Metals & Mining'),
('A10','Basic Materials - Other Precious Metals & Mining'),
('A11','Basic Materials - Paper & Paper products'),
('A12','Basic Materials - Silver'),
('A13','Basic Materials - Specialty Chemicals'),
('A14','Basic Materials - Steel'),
('B01','Communication Services - Advertising Agencies'),
('B02','Communication Services - Broadcasting'),
('B03','Communication Services - Electronic Gaming & Multimedia'),
('B04','Communication Services - Entertainment'),
('B05','Communication Services - Internet Content & Information'),
('B06','Communication Services - Publishing'),
('B07','Communication Services - Telecom Services'),
('C01','Consumer Cyclical - Apparel Manufacturing'),
('C02','Consumer Cyclical - Apparel Retail'),
('C03','Consumer Cyclical - Auto & Truck Dealerships'),
('C04','Consumer Cyclical - Auto Manufacturers'),
('C05','Consumer Cyclical - Auto Parts'),
('C06','Consumer Cyclical - Department Stores'),
('C07','Consumer Cyclical - Footwear & Accesories'),
('C08','Consumer Cyclical - Furnishings, Fixtures and Appliances'),
('C09','Consumer Cyclical - Gambling'),
('C10','Consumer Cyclical - Home Improvement Retail'),
('C11','Consumer Cyclical - Internet Retail'),
('C12','Consumer Cyclical - Leisure'),
('C13','Consumer Cyclical - Lodging'),
('C14','Consumer Cyclical - Luxury Goods'),
('C15','Consumer Cyclical - Packaging & Containers'),
('C16','Consumer Cyclical - Personal Services'),
('C17','Consumer Cyclical - Recreational Vehicles'),
('C18','Consumer Cyclical - Residential Construction'),
('C19','Consumer Cyclical - Resorts & Casinos'),
('C20','Consumer Cyclical - Restaurants'),
('C21','Consumer Cyclical - Specialty Retail'),
('C22','Consumer Cyclical - Textile Manufacturing'),
('C23','Consumer Cyclical - Travel services'),
('D01','Consumer Defensive - Beverages - Brewers'),
('D02','Consumer Defensive - Beverages - Non Alcoholic'),
('D03','Consumer Defensive - Beverages - Wineries & Distilleries'),
('D04','Consumer Defensive - Confectioners'),
('D05','Consumer Defensive - Discount Stores'),
('D06','Consumer Defensive - Education & Training Services'),
('D07','Consumer Defensive - Farm products'),
('D08','Consumer Defensive - Food Distribution'),
('D09','Consumer Defensive - Grocery Stores'),
('D10','Consumer Defensive - Household & Personal products'),
('D11','Consumer Defensive - Packaged Foods'),
('D12','Consumer Defensive - Tobacco'),
('E01','Energy - Oil & Gas Drilling'),
('E02','Energy - Oil & Gas E&P'),
('E03','Energy - Oil & Gas Equipment & Services'),
('E04','Energy - Oil & Gas Integrated'),
('E05','Energy - Oil & Gas Midstream'),
('E06','Energy - Oil & Gas Refining & Marketing'),
('E07','Energy - Thermal coal'),
('E08','Energy - Uranium'),
('F01','Financial - Asset Management'),
('F02','Financial - Banks - Diversified'),
('F03','Financial - Banks - Regional'),
('F04','Financial - Capital Markets'),
('F05','Financial - Credit Services'),
('F06','Financial - Financial Conglomerates'),
('F07','Financial - Financial Data & Stock Exchanges'),
('F08','Financial - Insurance - Diversified'),
('F09','Financial - Insurance - Life'),
('F10','Financial - Insurance - Property & Casualty'),
('F11','Financial - Insurance - Reinsurance'),
('F12','Financial - Insurance - Specialty'),
('F13','Financial - Insurance Brokers'),
('F14','Financial - Mortgage finance'),
('F15','Financial - Shell Companies'),
('G01','Healthcare - Biotechnology'),
('G02','Healthcare - Diagnostics & Research'),
('G03','Healthcare - Drug Manufacturers - General'),
('G04','Healthcare - Drug Manufacturers - Specialty & Generic'),
('G05','Healthcare - Health Information Services'),
('G06','Healthcare - Healthcare plans'),
('G07','Healthcare - Medical Care Facilities'),
('G08','Healthcare - Medical Devices'),
('G09','Healthcare - Medical Distribution'),
('G10','Healthcare - Medical Instruments & Supplies'),
('G11','Healthcare - Pharmaceutical Retailers'),
('H01','Industrials - Aerospace & Defense'),
('H02','Industrials - Airlines'),
('H03','Industrials - Airports & Air Services'),
('H04','Industrials - Building Products & Equipment'),
('H05','Industrials - Business Equipment & Supplies'),
('H06','Industrials - Conglomerates'),
('H07','Industrials - Consulting Services'),
('H08','Industrials - Electrical Equipment & parts'),
('H09','Industrials - Engineering & Construction'),
('H10','Industrials - Farm & Heavy Construction Machinery'),
('H11','Industrials - Industrial Distribution'),
('H12','Industrials - Integrated Freight & Logistics'),
('H13','Industrials - Marine Shipping'),
('H14','Industrials - Metal Fabrication'),
('H15','Industrials - Pollution & Treatment Controls'),
('H16','Industrials - Railroads'),
('H17','Industrials - Rental & Leasing Services'),
('H18','Industrials - Security & Protection Services'),
('H19','Industrials - Specialty Business Services'),
('H20','Industrials - Specialty Industrial Machinery'),
('H21','Industrials - Staffing & Employment Services'),
('H22','Industrials - Tools & Accessories'),
('H23','Industrials - Trucking'),
('H24','Industrials - Waste Management'),
('H25','Industrials - Infrastructure Operations'),        
('I01','Real Estate - Real Estate  Development'),
('I02','Real Estate - Real Estate  Diversified'),
('I03','Real Estate - Real Estate  Services'),
('I04','Real Estate - REIT - Diversified'),
('I05','Real Estate - REIT - Healthcare Facilities'),
('I06','Real Estate - REIT - Hotel & Motel'),
('I07','Real Estate - REIT - Industrial'),
('I08','Real Estate - REIT - Mortgage'),
('I09','Real Estate - REIT - Office'),
('I10','Real Estate - REIT - Residential'),
('I11','Real Estate - REIT - Retail'),
('I12','Real Estate - REIT - Specialty'),
('J01','Technology - Communication Equipment'),
('J02','Technology - Computer Hardware'),
('J03','Technology - Consumer Electronics'),
('J04','Technology - Electronic Components'),
('J05','Technology - Electronics & Computer Distribution'),
('J06','Technology - Information Technology Services'),
('J07','Technology - Scientific & Technical Instruments'),
('J08','Technology - Semiconductor Equipment & Materials'),
('J09','Technology - Semiconductors'),
('J10','Technology - Software - Application'),
('J11','Technology - Software - Infraestructure'),
('J12','Technology - Solar'),
('K01','Utilities - Diversified'),
('K02','Utilities - Independent Power Producers'),
('K03','Utilities - Regulated Electric'),
('K04','Utilities - Regulated Gas'),
('K05','Utilities - Regulated Water'),
('K06','Utilities - Renewable')]

dic_allindus = {'Basic Materials - Agricultural inputs': A01,'Basic Materials - Aluminum': A02,'Basic Materials - Building materials': A03,'Basic Materials - Chemicals': A04,'Basic Materials - Coking coal': A05,'Basic Materials - Copper': A06,'Basic Materials - Gold': A07,'Basic Materials - Lumber & Wood production': A08,'Basic Materials - Other Industrial Metals & Mining': A09,'Basic Materials - Other Precious Metals & Mining': A10,'Basic Materials - Paper & Paper products': A11,'Basic Materials - Silver': A12,'Basic Materials - Specialty Chemicals': A13,'Basic Materials - Steel': A14,'Communication Services - Advertising Agencies': B01,'Communication Services - Broadcasting': B02,'Communication Services - Electronic Gaming & Multimedia':B03,'Communication Services - Entertainment':B04,'Communication Services - Internet Content & Information':B05,'Communication Services - Publishing':B06,'Communication Services - Telecom Services':B07,'Consumer Cyclical - Apparel Manufacturing':C01,'Consumer Cyclical - Apparel Retail':C02,'Consumer Cyclical - Auto & Truck Dealerships':C03,'Consumer Cyclical - Auto Manufacturers':C04,'Consumer Cyclical - Auto Parts':C05,'Consumer Cyclical - Department Stores':C06,'Consumer Cyclical - Footwear & Accesories':C07,'Consumer Cyclical - Furnishings, Fixtures and Appliances':C08,'Consumer Cyclical - Gambling':C09,'Consumer Cyclical - Home Improvement Retail':C10,'Consumer Cyclical - Internet Retail':C11,'Consumer Cyclical - Leisure':C12,'Consumer Cyclical - Lodging':C13,'Consumer Cyclical - Luxury Goods':C14,'Consumer Cyclical - Packaging & Containers':C15,'Consumer Cyclical - Personal Services':C16,'Consumer Cyclical - Recreational Vehicles':C17,'Consumer Cyclical - Residential Construction':C18,'Consumer Cyclical - Resorts & Casinos':C19,'Consumer Cyclical - Restaurants':C20,'Consumer Cyclical - Specialty Retail':C21,'Consumer Cyclical - Textile Manufacturing':C22,'Consumer Cyclical - Travel services':C23,'Consumer Defensive - Beverages - Brewers':D01,'Consumer Defensive - Beverages - Non Alcoholic':D02,'Consumer Defensive - Beverages - Wineries & Distilleries':D03,'Consumer Defensive - Confectioners':D04,'Consumer Defensive - Discount Stores':D05,'Consumer Defensive - Education & Training Services':D06,'Consumer Defensive - Farm products':D07,'Consumer Defensive - Food Distribution':D08,'Consumer Defensive - Grocery Stores':D09,'Consumer Defensive - Household & Personal products':D10,'Consumer Defensive - Packaged Foods':D11,'Consumer Defensive - Tobacco':D12,'Energy - Oil & Gas Drilling':E01,'Energy - Oil & Gas E&P':E02,'Energy - Oil & Gas Equipment & Services':E03,'Energy - Oil & Gas Integrated':E04,'Energy - Oil & Gas Midstream':E05,'Energy - Oil & Gas Refining & Marketing':E06,'Energy - Thermal coal':E07,'Energy - Uranium':E08,'Financial - Asset Management':F01,'Financial - Banks - Diversified':F02,'Financial - Banks - Regional':F03,'Financial - Capital Markets':F04,'Financial - Credit Services':F05,'Financial - Financial Conglomerates':F06,'Financial - Financial Data & Stock Exchanges':F07,'Financial - Insurance - Diversified':F08,'Financial - Insurance - Life':F09,'Financial - Insurance - Property & Casualty':F10,'Financial - Insurance - Reinsurance':F11,'Financial - Insurance - Specialty':F12,'Financial - Insurance Brokers':F13,'Financial - Mortgage finance':F14,'Financial - Shell Companies':F15,'Healthcare - Biotechnology':G01,'Healthcare - Diagnostics & Research':G02,'Healthcare - Drug Manufacturers - General':G03,'Healthcare - Drug Manufacturers - Specialty & Generic':G04,'Healthcare - Health Information Services':G05,'Healthcare - Healthcare plans':G06,'Healthcare - Medical Care Facilities':G07,'Healthcare - Medical Devices':G08,'Healthcare - Medical Distribution':G09,'Healthcare - Medical Instruments & Supplies':G10,'Healthcare - Pharmaceutical Retailers':G11,'Industrials - Aerospace & Defense':H01,'Industrials - Airlines':H02,'Industrials - Airports & Air Services':H03,'Industrials - Building Products & Equipment':H04,'Industrials - Business Equipment & Supplies':H05,'Industrials - Conglomerates':H06,'Industrials - Consulting Services':H07,'Industrials - Electrical Equipment & parts':H08,'Industrials - Engineering & Construction':H09,'Industrials - Farm & Heavy Construction Machinery':H10,'Industrials - Industrial Distribution':H11,'Industrials - Integrated Freight & Logistics':H12,'Industrials - Marine Shipping':H13,'Industrials - Metal Fabrication':H14,'Industrials - Pollution & Treatment Controls':H15,'Industrials - Railroads':H16,'Industrials - Rental & Leasing Services':H17,'Industrials - Security & Protection Services':H18,'Industrials - Specialty Business Services':H19,'Industrials - Specialty Industrial Machinery':H20,'Industrials - Staffing & Employment Services':H21,'Industrials - Tools & Accessories':H22,'Industrials - Trucking':H23,'Industrials - Waste Management':H24,'Industrials - Infrastructure Operations':H25,'Real Estate - Real Estate  Development':I01,'Real Estate - Real Estate  Diversified':I02,'Real Estate - Real Estate  Services':I03,'Real Estate - REIT - Diversified':I04,'Real Estate - REIT - Healthcare Facilities':I05,'Real Estate - REIT - Hotel & Motel':I06,'Real Estate - REIT - Industrial':I07,'Real Estate - REIT - Mortgage':I08,'Real Estate - REIT - Office':I09,'Real Estate - REIT - Residential':I10,'Real Estate - REIT - Retail':I11,'Real Estate - REIT - Specialty':I12,'Technology - Communication Equipment':J01,'Technology - Computer Hardware':J02,'Technology - Consumer Electronics':J03,'Technology - Electronic Components':J04,'Technology - Electronics & Computer Distribution':J05,'Technology - Information Technology Services':J06,'Technology - Scientific & Technical Instruments':J07,'Technology - Semiconductor Equipment & Materials':J08,'Technology - Semiconductors':J09,'Technology - Software - Application':J10,'Technology - Software - Infraestructure':J11,'Technology - Solar':J12,'Utilities - Diversified':K01,'Utilities - Independent Power Producers':K02,'Utilities - Regulated Electric':K03,'Utilities - Regulated Gas':K04,'Utilities - Regulated Water':K05,'Utilities - Renewable':K06}
