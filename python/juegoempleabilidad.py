#Mata, Marko y Andoni
import time


preguntas = [
    {
        "pregunta": "¿Qué es la ITSS?",
        "opciones": [
            "Inspección de trabajo y seguridad social.",
            "Instituto Técnico de Servicios Sanitarios.",
            "International Technology Support System.",
            "Impuesto sobre Transacciones de Servicios Sociales."
        ],
        "correcta": 0
    },
    {
        "pregunta": "¿Cuál de estos no es un poder de la empresa?",
        "opciones": [
            "Dirección.",
            "Control.",
            "Disciplinario.",
            "Creativo absoluto."
        ],
        "correcta": 3
    },
    {
        "pregunta": "¿Puede la empresa grabarte en vídeo en tu puesto de trabajo?",
        "opciones": [
            "Sí, pero sin sonido.",
            "No, solo con sonido.",
            "Sí, pero con sonido y con color.",
            "No."
        ],
        "correcta": 0
    },
    {
        "pregunta": "¿Qué es la seguridad social?",
        "opciones": [
            "Un sistema privado de seguros médicos.",
            "Un organismo internacional de ayuda humanitaria.",
            "Un sistema público que protege a las personas ante situaciones como enfermedad, desempleo o jubilación.",
            "Un impuesto obligatorio para financiar a las empresas."
        ],
        "correcta": 2
    },
    {
        "pregunta": "¿Qué objetivo tiene la Seguridad Social?",
        "opciones": [
            "Aumentar los beneficios de las empresas privadas.",
            "Controlar el comercio internacional.",
            "Sustituir a los seguros privados.",
            "Garantizar la protección y el bienestar de las personas ante situaciones de necesidad."
        ],
        "correcta": 3
    },
    {
        "pregunta": "¿Cuáles son los principios básicos de la Seguridad Social?",
        "opciones": [
            "Competencia, privatización y rentabilidad.",
            "Jerarquía, disciplina y control económico.",
            "Individualismo, libre mercado y beneficio empresarial.",
            "Universalidad, solidaridad e igualdad."
        ],
        "correcta": 3
    },
    {
        "pregunta": "¿Cuál es la diferencia más característica de una prestación contributiva o no contributiva?",
        "opciones": [
            "La cuantía económica que se cobra.",
            "El organismo que la gestiona.",
            "La duración de la prestación.",
            "Que la contributiva exige haber cotizado previamente y la no contributiva no."
        ],
        "correcta": 3
    },
    {
        "pregunta": "¿Qué prestaciones tiene la Seguridad Social?",
        "opciones": [
            "Solo pensiones de jubilación.",
            "Únicamente asistencia sanitaria.",
            "Ayudas privadas gestionadas por bancos.",
            "Asistencia sanitaria y prestaciones económicas (jubilación, incapacidad, desempleo, viudedad, etc.)."
        ],
        "correcta": 3
    },
    {
        "pregunta": "¿Cuántas semanas retribuidas te dan por baja de maternidad?",
        "opciones": [
            "1 semana.",
            "19 semanas.",
            "44 semanas.",
            "30 semanas."
        ],
        "correcta": 1
    },
    {
        "pregunta": "¿Qué regula el SEPE?",
        "opciones": [
            "Jubilación",
            "Nacimiento de un niño",
            "El paro",
            "Las bajas"
        ],
        "correcta": 2
    },
    {
        "pregunta": "¿Cuántos días tienes que haber cotizado para la prestación por desempleo?",
        "opciones": [
            "Haber cotizado al menos 360 días en los últimos 6 años.",
            "Haber cotizado al menos 180 días en toda la vida laboral.",
            "Haber trabajado al menos 5 años continuos sin cotizar.",
            "Haber cotizado solamente días en contratos a tiempo parcial."
        ],
        "correcta": 0
    },
    {
        "pregunta": "¿Cuántos años tienes que haber trabajado para jubilarte?",
        "opciones": [
            "Haber cotizado al menos 15 años.",
            "Haber trabajado solo 5 años sin cotizar.",
            "Haber trabajado 50 años exactamente.",
            "Haber cotizado únicamente 1 año."
        ],
        "correcta": 0
    },
    {
        "pregunta": "Si te has hecho un esguince en tu casa te dan incapacidad temporal y ¿te pagan?",
        "opciones": [
            "Sí, desde el primer día",
            "Sí, a partir del cuarto día",
            "No te pagan",
            "Te pagan la mitad del sueldo"
        ],
        "correcta": 1
    }
]

{
        "pregunta": "¿Cómo se les llama también a los trabajadores por cuenta propia?",
        "opciones": ["Empleado", "Turista", "Autónomo", "Único"],
        "correcta": 2
    },
    {
        "pregunta": "¿Cómo se llama el requisito en el que el empresario da órdenes en una relación laboral?",
        "opciones": ["Cuenta ajena", "Dependiente", "Funcionario", "Retribuida"],
        "correcta": 1
    },
    {
        "pregunta": "Las relaciones laborales de carácter especial se distinguen porque:",
        "opciones": [
            "Son informales y sin contrato",
            "Son laborales, pero con normas especiales",
            "No son sobre el salario",
            "Solo aplican a directores"
        ],
        "correcta": 1
    },
    {
        "pregunta": "¿Qué significa norma mínima?",
        "opciones": [
            "Que ninguna norma inferior puede condicionar más que una superior",
            "Que la norma tiene mínimo condicionamiento",
            "Que la norma es pequeña",
            "Todas son correctas"
        ],
        "correcta": 0
    },
    {
        "pregunta": "La huelga es derecho básico:",
        "opciones": ["Verdadero", "Falso"],
        "correcta": 0
    },
    {
        "pregunta": "¿Qué ley está arriba del todo en la jerarquía?",
        "opciones": [
            "Constitución Europea",
            "Normativa Europea",
            "Convenio colectivo",
            "Estatuto del trabajador"
        ],
        "correcta": 1
    },
    {
        "pregunta": "¿Cuándo debe formalizarse por escrito el contrato indefinido?",
        "opciones": ["Nunca", "Siempre", "Con contrato parcial", "Todas son correctas"],
        "correcta": 2
    },
    {
        "pregunta": "¿Qué contrato se hace a un socorrista que trabaja solo en verano?",
        "opciones": ["Formativo", "Prácticas", "Fijo discontinuo", "Cualquiera"],
        "correcta": 2
    },
    {
        "pregunta": "Contrato para incrementos ocasionales e imprevisibles:",
        "opciones": [
            "Temporal de producción",
            "Temporal por sustitución",
            "Temporal por jubilación",
            "Prácticas"
        ],
        "correcta": 0
    },
    {
        "pregunta": "Contrato para cubrir la ausencia de un trabajador:",
        "opciones": [
            "Producción",
            "Jubilación",
            "Prácticas",
            "Sustitución"
        ],
        "correcta": 3
    },
    {
        "pregunta": "El contrato formativo en alternancia sirve para:",
        "opciones": [
            "Combinar formación y trabajo remunerado",
            "Desempleados",
            "Estudiantes",
            "Jubilados"
        ],
        "correcta": 0
    },
    {
        "pregunta": "Duración máxima del contrato de prácticas:",
        "opciones": ["2 años", "1 año", "6 meses", "1 año y medio"],
        "correcta": 0
    },
    {
        "pregunta": "¿Cuándo se usa el contrato de relevo?",
        "opciones": [
            "Cambio de turno",
            "Cambio de horario",
            "Por jubilación parcial",
            "Traspaso familiar"
        ],
        "correcta": 2
    },
    {
        "pregunta": "Trabajo legal de menores:",
        "opciones": [
            "15 años diurno",
            "17 nocturno",
            "16 diurno con permiso",
            "14 con permiso"
        ],
        "correcta": 2
    },
    {
        "pregunta": "Descanso mínimo cada 6 horas:",
        "opciones": ["15 min", "20 min", "25 min", "30 min"],
        "correcta": 0
    },
    {
        "pregunta": "Plazo para aceptar adaptación de jornada:",
        "opciones": ["7 días", "14 días", "8 días", "15 días"],
        "correcta": 3
    },
    {
        "pregunta": "Salario en especie máximo:",
        "opciones": ["15%", "21%", "25%", "30%"],
        "correcta": 3
    },
    {
        "pregunta": "Vacaciones mínimas por ley:",
        "opciones": [
            "20 y 60",
            "30 y 60",
            "30 sin máximo",
            "20 sin máximo"
        ],
        "correcta": 2
    },
    {
        "pregunta": "¿Qué NO es salario?",
        "opciones": [
            "Dinero por trabajo",
            "Salario en especie",
            "Indemnizaciones",
            "Descansos"
        ],
        "correcta": 2
    },
    {
        "pregunta": "¿Qué paga la Seguridad Social?",
        "opciones": [
            "El paro",
            "Seguridad privada",
            "Todas correctas",
            "Ninguna"
        ],
        "correcta": 0
    }


def jugar():
    print("🎮 BIENVENIDO AL KAHOOT DE SEGURIDAD SOCIAL 🎮\n")
    nombre = input("Introduce tu nombre: ")
    puntos = 0

    for i, q in enumerate(preguntas, start=1):
        print(f"\nPregunta {i}: {q['pregunta']}\n")

        for idx, opcion in enumerate(q["opciones"], start=1):
            print(f"{idx}. {opcion}")

        try:
            respuesta = int(input("\nTu respuesta (1-4): ")) - 1
        except:
            print("Respuesta inválida ❌")
            continue

        if respuesta == q["correcta"]:
            print("✅ ¡Correcto!")
            puntos += 1
        else:
            print("❌ Incorrecto.")
            correcta = q["opciones"][q["correcta"]]
            print(f"Respuesta correcta: {correcta}")

        time.sleep(1)

    print("\n🏁 JUEGO TERMINADO 🏁")
    print(f"Jugador: {nombre}")
    print(f"Puntuación: {puntos}/{len(preguntas)}")

    if puntos == len(preguntas):
        print("🎉 ¡Perfecto! ¡Eres un crack!")
    elif puntos >= len(preguntas) * 0.7:
        print("👏 ¡Muy buen resultado!")
    elif puntos >= len(preguntas) * 0.4:
        print("🙂 Aprobado.")
    else:
        print("📚 Necesitas repasar un poco más.")


if __name__ == "__main__":
    jugar()
