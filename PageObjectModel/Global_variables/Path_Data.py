class PathAndVariablesUtil:

    @staticmethod
    def home():
        home = None
        home = "Inicio"
        return home

    @staticmethod
    def social():
        social = None
        social = "Social"
        return social

    @staticmethod
    def glucose():
        glucose = None
        glucose = "Glucosa"
        return glucose

    @staticmethod
    def challenge():
        challenge = None
        challenge = "Retos"
        return challenge

    @staticmethod
    def benefits():
        benefits = None
        benefits = "Beneficios"
        return benefits

    @staticmethod
    def chats():
        chats = None
        chats = "Chats"
        return chats

    @staticmethod
    def value_nav():
        a = None
        a = 5
        return a

    @staticmethod
    def db_path():  # Ruta para acceder a los archivos de Base de Dato, Excel, imagenes de se soporte, etc.
        path_rute_DB = None
        path_rute_DB = "C:/Users/user/Documents/Habits.ai/Automatizacion/qa_automation"
        return path_rute_DB

    @staticmethod
    def evidence_path():  # Ruta para almacenar evidencia de pruebas (screenshot)
        path_rute_Evidence = None
        path_rute_Evidence = "C:\\Users\\user\\Documents\\Habits.ai\\Automatizacion\\qa_automation"
        return path_rute_Evidence

    @staticmethod
    def challenge_navbar():  # Variable de navegacion en el navbar seccion Retos
        path_rute_challenge = None
        num = None
        num = PathAndVariablesUtil.value_nav()
        path_rute_challenge = f"//android.widget.TextView[@text='{PathAndVariablesUtil.challenge()}']"
        return path_rute_challenge

    @staticmethod
    def home_navbar():  # Variable de navegacion en el navbar seccion Home
        path_home_navbar = None
        num = None
        num = PathAndVariablesUtil.value_nav()
        path_home_navbar = f"//android.widget.TextView[@text='{PathAndVariablesUtil.home()}']"
        return path_home_navbar

    @staticmethod
    def benefits_navbar():  # Variable de navegacion en el navbar seccion Beneficios
        path_benefits_navbar = None
        num = None
        num = PathAndVariablesUtil.value_nav()
        path_benefits_navbar = f"//android.widget.TextView[@text='{PathAndVariablesUtil.benefits()}']"
        return path_benefits_navbar

    @staticmethod
    def chats_navbar():  # Variable de navegacion en el navbar seccion Chats
        path_chat_navbar = None
        num = None
        num = PathAndVariablesUtil.value_nav()
        path_chat_navbar = f"//android.widget.TextView[@text='{PathAndVariablesUtil.chats()}']"
        return path_chat_navbar

    @staticmethod
    def social_navbar():  # Variable de navegacion en el navbar seccion Social
        path_social_navbar = None
        num = None
        num = PathAndVariablesUtil.value_nav()
        path_social_navbar = f"//android.widget.TextView[@text='{PathAndVariablesUtil.social()}']"
        return path_social_navbar

    # @staticmethod
    # def ana_navbar():  # Variable de navegacion en el navbar seccion Ana
    #     path_ana_navbar = None
    #     num = None
    #     num = PathAndVariablesUtil.value_nav()
    #     path_ana_navbar = f"//android.widget.Button[@content-desc=', tab, 4 of {num}']/android.view.ViewGroup"
    #     return path_ana_navbar

    # @staticmethod
    # def awards_navbar():  # Variable d navegacion para premios
    #     path_awards_navbar = None
    #     num = None
    #     num = PathAndVariablesUtil.value_nav()
    #     path_awards_navbar = f"//android.widget.Button[@content-desc=', tab, 4 of {num}']/android.view.ViewGroup"
    #     return path_awards_navbar

    @staticmethod
    def glucosa_navbar():
        path_glucosa_navbar = None
        num = None
        num = PathAndVariablesUtil.value_nav()
        path_glucosa_navbar = f"//android.widget.TextView[@text='{PathAndVariablesUtil.glucose()}']"

    @staticmethod
    def cod_licencia():
        variable_company_licencia = None
        variable_company_licencia = "ENT-PRI"
        return variable_company_licencia

    @staticmethod
    def cod_habits():
        variable_company_habits = None
        variable_company_habits = "HAB-BTA"
        return variable_company_habits

    @staticmethod
    def SetUpDeviceName():
        devicename = None
        devicename = "lancelot"
        return devicename

    @staticmethod
    def SetUpPlatform():
        platfomrdevice = None
        platfomrdevice = "Android"
        return platfomrdevice

    @staticmethod
    def SetUpVersion():
        versionplatform = None
        versionplatform = "12"
        return versionplatform

    @staticmethod
    def base():
        base = None
        base="https://apiv2desarrollo.habits.ai"
        return  base