from os import getenv
from dotenv import load_dotenv

load_dotenv()

class Config:
    def __init__(self):
        self.API_ID = int(getenv("37862320", 0))
        self.API_HASH = getenv("cdb4a59a76fae6bd8fa42e77455f8697")

        self.BOT_TOKEN = getenv("8341511264:AAFjNIOYE5NbABPloFbz-r989l2ySRUs988")
        self.MONGO_URL = getenv("mongodb+srv://lelopthaapa_db_user:Ronin1122@cluster0.doimgh0.mongodb.net/?retryWrites=true&w=majority")

        self.LOGGER_ID = int(getenv("LOGGER_ID", 0))
        self.OWNER_ID = int(getenv("OWNER_ID", 0))

        self.DURATION_LIMIT = int(getenv("DURATION_LIMIT", 60)) * 60
        self.QUEUE_LIMIT = int(getenv("QUEUE_LIMIT", 20))
        self.PLAYLIST_LIMIT = int(getenv("PLAYLIST_LIMIT", 20))

        self.SESSION1 = getenv("SESSION", "BQJBu7AAhhG6MmNUFoqJukQOFZDPl5I4QrcapymDjzK5XNYTqaofTEqI5v12xgg0_xkARp-oRG0bXkUhmRB5ziTmjbDSh4I0ty2tGheoT6-mEzOYIsUKMXRuNfAb-Li9eAvlokTfxwCVa9HTBnOD3cPe_plNAUpRuyk5FtUmdeV5Wu_lWcE5cRECGnW0SHO24GiyHoK8jK6BAVL25rVnwLqktC1O2IZn3cam0hCs2ZqSF_B_4Z-8cuREGMaO8IrRnhOl3adW5sUzlOz14FmrHlGeyAL_s8Cb0tgFbST6EAFW25MWVv_0FG_cKbAxWCoR7u9uG4AhX6NrG3g3Z3ZB53N06rEL8AAAAAHQ8OAyAA")
        self.SESSION2 = getenv("SESSION2", None)
        self.SESSION3 = getenv("SESSION3", None)

        self.SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/FallenAssociation")
        self.SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/DevilsHeavenMF")

        self.AUTO_LEAVE: bool = getenv("AUTO_LEAVE", False)
        self.VIDEO_PLAY: bool = getenv("VIDEO_PLAY", True)
        self.DEFAULT_THUMB = getenv("DEFAULT_THUMB", "https://te.legra.ph/file/3e40a408286d4eda24191.jpg")
        self.PING_IMG = getenv("PING_IMG", "https://files.catbox.moe/haagg2.png")
        self.START_IMG = getenv("START_IMG", "https://files.catbox.moe/zvziwk.jpg")

    def check(self):
        missing = [
            var
            for var in ["API_ID", "API_HASH", "BOT_TOKEN", "MONGO_URL", "LOGGER_ID", "OWNER_ID", "SESSION1"]
            if not getattr(self, var)
        ]
        if missing:
            raise SystemExit(f"Missing required environment variables: {', '.join(missing)}")
