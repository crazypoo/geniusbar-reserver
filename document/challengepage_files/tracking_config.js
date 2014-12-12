trackingConfig = {
	Prefix : "concierge",   
	
	Rule_Lookup : {
		TECHSUPPORT: "genius bar",
		TRAINING: "onetoone training",
		WORKSHOP: "workshop",
		SHOPPING: "personal shopping",
		BIZ_CONSULT: "business consultation",
		O2OWORKSHOP: "onetoone workshop",
		O2OPERSONALPROJECT: "onetoone personal project",
		PROLAB: "prolab",
		ONETOONE: "onetoone group workshop",
		YOUTH: "youth",
		CAMP: "camp",
		FIELDTRIP: "field trip",
		UNKNOWN: "unknown"
	}, 
	
	ServiceType_Lookup : {
		"4d": "mac",
		"5c": "mac", 
		"70": "mac",
		"6f": "ipod",
		"54": "ipod",
 	   	"71": "iphone",
	   	"9e": "iphone", 
		"1" : "AppleTV",
		"75" : "backup consultation",
		"15" : "consultation",  
		"4e" : "tune up",  
		"UNKNOWN": "none"
	},
	
	Env_Lookup : {
		"web": "web",
		"kiosk": "kiosk",
		"o2oportal": "o2oportal"
	},

	Page_Lookup : {  
		RulePickerPage: " rule picker",
		TopicPickerPage: "topic picker",
		TimePickerPage: "time picker",
		WorkshopBrowserPage: "workshop browser",
		ReservationConfirmationPage: "reservation confirmation",

		GuestSignInPage: "guest signin",
		AppleIDSignInPage: "appleid signin",
		CreateAppleIDPage: "create appleid",
		AddMembershipPage: "add membership",
		AdditionalInformationPage: "additional information",
		ReviewAppleIDPage: "review appleid",
		CreateAppleIDSuccessPage: "create appleid success",
		MakeAReservationPage: " make a reservation",

		ReservationHistoryPage: "reservation history",
		MyProfilePage: "my profile",

		PersonalSetupStep1: "personalsetup step1",
		PersonalSetupStep2: "personalsetup step2",
		PersonalSetupStep3: "personalsetup step3",
		PersonalSetupStep4: "personalsetup step4",
		PSConfirmationPage: "personalsetup confirmation",
		QuickDropPage: "quickdrop",
		QuickDropConfirmationPage: "quickdrop confirmation",

		ProLabsPage: "prolabs",
		CampPage: "camp",
		FieldTripStep1Page: "fieldtrip step1",
		FieldTripStep2Page: "fieldtrip step2",
		YouthWorkshopPage: "youth workshop",
		GroupWorkshopConfirmationPage: "group workshop confirmation",

		ReservationErrorPage: "reservation error",
		KioskiForgotPage: "kiosk iforgot",
		InvalidBrowserPage: "invalid browser",
		ErrorPage: "error",
			
		ConciergeSplit: "CAS split page"
	},     

	Link_Lookup : {
		timepicker_next: "right arrow",
		timepicker_previous: "left arrow",
		timepicker_openDropDown: "check availability",
		timepicker_mapOverlayAction: "map",
		reservationConfirmation_commentsOverlayAction: "comment",  
		reservationConfirmation_mapOverlayAction: "map",  
		worshopbrowser_toggleMoreStores: "check availability",
		worshopbrowser_mapOverlayAction: "map",
		worshopbrowser_tip_isShown: "i button",  
		cancelReservation_isShown: "cancel reservation",
		UNKNOWN: "unknown"
	},
	
	Account_Lookup: {
		"en": "appleglobal,appleretail,appleusconcierge",
		"en_US": "appleglobal,appleretail,appleusconcierge",
		"en_GB": "appleukglobal,appleukretail,appleukconcierge",
		"en_CA": "applecaglobal,applecaretail,applecaconcierge",
		"fr_CA": "applecaglobal,applecaretail,applecaconcierge",
		"fr_FR": "applefrglobal,applefrretail,applefrconcierge",
		"it_IT": "appleitglobal,appleitretail,appleitconcierge",
		"fr_CH": "applecrglobal,applecrretail,applecrconcierge",
		"de_CH": "appleceglobal,appleceretail,applececoncierge",
		"de": "appledeglobal,applederetail,appledeconcierge",
		"de_DE": "appledeglobal,applederetail,appledeconcierge",
		"zh_CN": "applecnglobal,applecnretail,applecnconcierge",
		"ja_JP": "applejpglobal,applejpretail,applejpconcierge",
		"en_AU": "appleauglobal,appleauretail,appleauconcierge",
		"test": "devapple"
	},
	
	Channel_Lookup: {
		"en": "www.us.retail.concierge",
		"en_US": "www.us.retail.concierge",
		"en_GB": "www.uk.retail.concierge",
		"en_CA": "www.ca.retail.concierge",
		"fr_CA": "www.ca.fr.retail.concierge",
		"fr_FR": "www.fr.retail.concierge",
		"it_IT": "www.it.retail.concierge",
		"fr_CH": "www.cr.retail.concierge",
		"de_CH": "www.ce.retail.concierge",
		"de": "www.de.retail.concierge",
		"de_DE": "www.de.retail.concierge",
		"zh_CN": "www.cn.retail.concierge",
		"ja_JP": "www.jp.retail.concierge",
		"en_AU": "www.au.retail.concierge",
		"test": "www.us.retail.concierge"
	},
	
	Account_Lookup_Replacement: {
		"en": "appleglobal,appleretail,appleusconcierge,applesupport",
		"en_US": "appleglobal,appleretail,appleusconcierge,applesupport",
		"en_GB": "appleukglobal,appleukretail,appleukconcierge,appleuksupport",
		"en_CA": "applecaglobal,applecaretail,applecaconcierge,applecasupport",
		"fr_CA": "applecaglobal,applecaretail,applecaconcierge,applecasupport",
		"fr_FR": "applefrglobal,applefrretail,applefrconcierge,applefrsupport",
		"it_IT": "appleitglobal,appleitretail,appleitconcierge,appleitsupport",
		"fr_CH": "applecrglobal,applecrretail,applecrconcierge,applecrsupport",
		"de_CH": "appleceglobal,appleceretail,applececoncierge,applecesupport",
		"de": "appledeglobal,applederetail,appledeconcierge,appledesupport",
		"de_DE": "appledeglobal,applederetail,appledeconcierge,appledesupport",
		"zh_CN": "applecnglobal,applecnretail,applecnconcierge,applecnsupport",
		"ja_JP": "applejpglobal,applejpretail,applejpconcierge,applejpsupport",
		"en_AU": "appleauglobal,appleauretail,appleauconcierge,appleausupport",
		"test": "applesupport,devapple"
	}
	
};