from typing import Dict, Any, Coroutine
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import *
import json
import logging

"""Token"""
token = '6360134762:AAEKs4sxvXKAffJsVV0V4UWZANAySMLiAxc'
JSON_FILE_PATH = 'database.json'
"""Status bot telegram"""
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)
user_anno = 0
"""Vari message heandler"""
SCELTA, LEZIONI, LAUREE, ESAMI = range(4)
END = ConversationHandler.END

PRIMA = [["Lezioni", "Esami", "Lauree"]]



async def facts_to_str(user_data: Dict[str, str]) -> str:
    """Helper function for formatting the gathered user info."""
    facts = [f"{key} - {value}" for key, value in user_data.items()]
    return "\n".join(facts).join(["\n", "\n"])


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Inizia la conversazione e chiede all'utente che anno frequenta."""

    await update.message.reply_text(
        "Benvenuto! Io sono il Bot che ti ricerca le Lezioni/Esami/Lauree."
        "Invia /cancel per smettere di parlare con me.\n\n"
        "Cosa stai cercando?",
        reply_markup=ReplyKeyboardMarkup(
            PRIMA, one_time_keyboard=True, input_field_placeholder="?"
        )
    )
    print(SCELTA)
    return SCELTA


async def scelta(update: Update, context: ContextTypes.DEFAULT_TYPE, ) -> int:
    user_data = context.user_data
    text = update.message.text
    context.user_data["choice"] = text
    user_data = user_data["choice"]
    print("prima scelta ", user_data)

    reply_keyboard = [["Primo anno", "Secondo anno", "Terzo anno"]]

    await update.message.reply_text(
        "Di quale anno sei interessato/a?",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="?"
        ),
    )

    print(LEZIONI)
    return LEZIONI


async def esami(update: Update, context: ContextTypes.DEFAULT_TYPE, ) -> int:
    user_data = context.user_data
    text = update.message.text
    context.user_data["choice"] = text
    user_data = user_data["choice"]
    print("prima scelta ", user_data)

    reply_keyboard = [["Esami primo anno", "Esami secondo anno", "Esami terzo anno"]]

    await update.message.reply_text(
        "Di quale anno sei interessato/a?",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="?"
        ),
    )

    print(ESAMI)
    return ESAMI


async def anno(update: Update, context: ContextTypes.DEFAULT_TYPE) -> Coroutine[Any, Any, int]:
    """Se entra in anno deve scegliere l'anno che vuole visionare le lezioni"""

    user_data = context.user_data
    text = update.message.text
    context.user_data["choice"] = text
    user_data = user_data["choice"]
    print("seconda scelta ", user_data)
    file = open('database.json')
    data = json.load(file)
    if "Primo anno" in user_data:
        lezioni_primo_anno = data.get('Lezioni_primo_anno', [])
        formatted_data = '\n\n'.join([
            f"{lezione['Materia : ']} \n- Docente: {lezione['Docente : ']}\nOrario: {lezione['Orario : ']}\nAula: {lezione['Aula : ']}"
            f"\nLink video-lezione: {lezione['Link : ']}"
            for lezione in lezioni_primo_anno])
        await update.message.reply_text(formatted_data)
    elif "Secondo anno" in user_data:
        lezioni_secondo_anno = data.get('Lezioni_secondo_anno', [])
        formatted_data = '\n\n'.join([
            f"{lezione['Materia : ']} \n- Docente: {lezione['Docente : ']}\nOrario: {lezione['Orario : ']}\nAula: {lezione['Aula : ']}"
            f"\nLink video-lezione: {lezione['Link : ']}"
            for lezione in lezioni_secondo_anno])
        await update.message.reply_text(formatted_data)
    elif "Terzo anno"  in user_data:
        lezioni_terzo_anno = data.get('Lezioni_terzo_anno', [])
        formatted_data = '\n\n'.join([
            f"{lezione['Materia : ']} \n- Docente: {lezione['Docente : ']}\nOrario: {lezione['Orario : ']}\nAula: {lezione['Aula : ']}"
            f"\nLink video-lezione: {lezione['Link : ']}"
            for lezione in lezioni_terzo_anno])
        await update.message.reply_text(formatted_data)

    elif "Esami primo anno" in user_data:
        Esami_primo_anno = data.get('Esami_primo_anno', [])
        formatted_data = '\n\n'.join([
            f"{lezione['Materia : ']} \n- Docente: {lezione['Docente : ']}\nOrario: {lezione['Orario : ']}\nAula: {lezione['Aula : ']}"
            f"\nLink esame: {lezione['Link : ']}"
            for lezione in Esami_primo_anno])
        await update.message.reply_text(formatted_data)

    elif "Esami secondo anno" in user_data:
        Esami_secondo_anno = data.get('Esami_secondo_anno', [])
        formatted_data = '\n\n'.join([
            f"{lezione['Materia : ']} \n- Docente: {lezione['Docente : ']}\nOrario: {lezione['Orario : ']}\nAula: {lezione['Aula : ']}"
            f"\nLink esame: {lezione['Link : ']}"
            for lezione in Esami_secondo_anno])
        await update.message.reply_text(formatted_data)

    elif "Esami terzo anno" in user_data:
        Esami_terzo_anno = data.get('Esami_terzo_anno', [])
        formatted_data = '\n\n'.join([
            f"{lezione['Materia : ']} \n- Docente: {lezione['Docente : ']}\nOrario: {lezione['Orario : ']}\nAula: {lezione['Aula : ']}"
            f"\nLink esame: {lezione['Link : ']}"
            for lezione in Esami_terzo_anno])
        await update.message.reply_text(formatted_data)

    else:
        await update.message.reply_text("Non ho trovato niente che corrisponda a quello che mi hai chiesto riprova scrivendo\n /cancel e riavvia il bot")
        return 0
    return scelta(SCELTA, None)


async def lauree(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Se entra in lauree visualizza tutte le date delle laure del dipartimento"""

    user = update.message.from_user
    logger.info("Utente: %s ha scelto lauree.", user.first_name)
    user_data = context.user_data
    text = update.message.text
    context.user_data["choice"] = text
    user_data = user_data["choice"]
    print("scelta ", user_data)
    file = open('database.json')
    data = json.load(file)
    await update.message.reply_text("Ecco a te le date delle prossime lauree :")
    Lauree_2023 = data.get('Lauree 2023-2024', [])
    formatted_data = '\n\n'.join([
        f"Data: {lezione['Data : ']} , \nOrario: {lezione['Orario : ']},"
        f"\nLink aula : {lezione['Link : ']}"
        for lezione in Lauree_2023])
    await update.message.reply_text(formatted_data)

    return SCELTA


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Cancella la conversazione."""
    user = update.message.from_user
    user_data = context.user_data
    logger.info("Utente: %s ha cancellato la conversazione.", user.first_name)
    await update.message.reply_text(
        "Grazie per aver utilizzato il bot. A presto...", reply_markup=ReplyKeyboardRemove()
    )
    user_data.clear()
    return ConversationHandler.END


def main() -> None:
    """Run the bot."""

    application = Application.builder().token(token).build()
    application.add_handler(CallbackQueryHandler(scelta, pattern='back'))
    application.add_handler(ConversationHandler(entry_points=[CommandHandler("start", start)],
                                                states={
                                                    SCELTA: [MessageHandler(filters.Regex("^Lezioni$"),
                                                                            scelta),
                                                             MessageHandler(filters.Regex("^Lauree$"), lauree),
                                                             MessageHandler(filters.Regex("^Esami$"), esami)],

                                                    ESAMI: [MessageHandler(filters.Regex(
                                                        "^(Esami primo anno|Esami secondo anno|Esami terzo anno)$"),
                                                        anno)],
                                                    LEZIONI: [MessageHandler(
                                                        filters.Regex("^(Primo anno|Secondo anno|Terzo anno)$"), anno)],

                                                    LAUREE: [MessageHandler(filters.Regex("^Lauree$"), lauree)]
                                                },

                                                fallbacks=[CommandHandler('cancel', cancel)
                                                           ],
                                                map_to_parent={
                                                    END: SCELTA
                                                }))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
