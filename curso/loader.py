from curso.models import *
import json

# Primeiro, limpar os dados existentes para evitar duplicações
Curso.objects.all().delete()
AreaCientifica.objects.all().delete()
Disciplina.objects.all().delete()

# Carregando e criando Áreas Científicas
areas_cientificas = {}
with open('curso/json/area_cientifica.json', encoding='utf-8') as file:
    areas = json.load(file)
    for area in areas:
        area_cientifica, _ = AreaCientifica.objects.get_or_create(
            nome=area['area_cientifica']
        )
        areas_cientificas[area['disciplina']] = area_cientifica

# Carregando dados do arquivo JSON para o curso e disciplinas
with open('curso/json/lig.json', encoding='utf-8') as file:
    data = json.load(file)
    course_detail = data['courseDetail']
    course_flat_plan = data['courseFlatPlan']

    # Criação do Curso
    curso = Curso.objects.create(
        nome=course_detail['courseName'],
        apresentacao=course_detail['presentation'],
        objetivos=course_detail['objectives'],
        competencias=course_detail['competences']
    )

    # Criação das Disciplinas
    for item in course_flat_plan:
        disciplina = Disciplina.objects.create(
            nome=item['curricularUnitName'],
            ano=item['curricularYear'],
            semestre=['semester'],
            ects=item['ects'],
            curricularIUnitReadableCode=item['curricularIUnitReadableCode'],
            area_cientifica=areas_cientificas.get(item['curricularUnitName'])
        )

print("Dados importados com sucesso.")