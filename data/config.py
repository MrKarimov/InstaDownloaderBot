from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = "BOT_TOKEN"  # Bot toekn
ADMINS = ["YOUR TELEGRAM ID"] # adminlar ro'yxati
# IP = env.str("ip")  # Xosting ip manzili
