import toutes_les_classes


def display_data_base(data_base):
    for a, b in data_base.items():
        print(a, " :", b)


def add_worker(complete_name):
    if complete_name not in data_base:
        worker = type_worker()
        print()
        if worker == "Administration":
            worker_administration = app.Administration()
            worker_administration_infos = worker_administration.display_information()
            data_base[complete_name] = worker_administration_infos
        elif worker == "Enseignant":
            worker_teacher = app.Teacher()
            worker_teacher_infos = worker_teacher.display_information()
            data_base[complete_name] = worker_teacher_infos
        elif worker == "Etudiant":
            worker_student = app.Student()
            worker_student_infos = worker_student.display_information()
            data_base[complete_name] = worker_student_infos
        elif worker == "Entretien":
            worker_maintenance = app.Maintenance()
            worker_maintenance_infos = worker_maintenance.display_information()
            data_base[complete_name] = worker_maintenance_infos
    else:
        print(f"{complete_name} existe déjà dans la base de données !")


def remove_worker(complete_name):
    if complete_name not in data_base:
        print(f"{complete_name} n'existe pas dans la base de données !")
    else:
        del data_base[complete_name]
        print(f"{complete_name} a été supprimé de la base de données.")


def save_data_base(chemin, data_base):
    with open(chemin, "w", encoding='utf-8') as f:
        json.dump(data_base, f, indent=4)


def type_worker():
    worker = input("Quel travailleur voulez-vous ajouter (Administration, Enseignant, Etudiant, Entretien) ? ")
    liste_worker = ["Administration", "Enseignant", "Etudiant", "Entretien"]
    if worker.capitalize() not in liste_worker:
        print("Veillez choisir un travailleur parmit la liste entre parenthèse !")
        type_worker()
    return worker.capitalize()

