class EmailAlert():

    def __init__(self):
        self.emailSent = False

    def sendEmailAlert(self,):
        self.emailSent = True


class LEDAlert():

    def __init__(self):
        self.ledGlows = False

    def glowLed(self,):
        self.ledGlows = True    


class StatsAlerter():

    def __init__(self,threshold,emailAlert,ledAlert):
        self.threshold = threshold
        self.emailAlert = emailAlert
        self.ledAlert = ledAlert

    def checkAndAlert(self,numbers):
        if(max(numbers) > self.threshold):
            self.emailAlert.sendEmailAlert()
            self.ledAlert.glowLed()

    