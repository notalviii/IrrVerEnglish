"""
Translation system for IrrVerEnglish.
Provides multilingual support for UI elements.
"""

class Translations:
    """Translation dictionary for UI elements."""

    TRANSLATIONS = {
        'en': {
            # Navigation
            'nav_home': 'Home',
            'nav_study': 'Study',
            'nav_verbs': 'Verbs',
            'nav_statistics': 'Statistics',
            'nav_settings': 'Settings',
            'nav_about': 'About',

            # Home page
            'home_welcome': 'Welcome to IrrVerEnglish',
            'home_description': 'Learn and practise English irregular verbs with interactive quizzes.\nImport your own CSV files and customize your learning experience.',
            'home_csv_file': 'CSV File',
            'home_csv_not_loaded': 'Not loaded',
            'home_csv_loaded': 'Loaded',
            'home_available_verbs': 'Available Verbs',
            'home_creator': 'Creator',
            'home_quick_actions': 'Quick Actions',
            'home_import_csv': 'Import CSV',
            'home_start_quiz': 'Start Quiz',
            'home_view_verbs': 'View Verbs',

            # Verbs page
            'verbs_title': 'Verbs Management',
            'verbs_import': 'Import CSV File',
            'verbs_loaded': 'Loaded',
            'verbs_verbs': 'verbs',
            'verbs_select_all': 'Select All',
            'verbs_deselect_all': 'Deselect All',
            'verbs_invert': 'Invert Selection',
            'verbs_range': 'Select by Row Range',
            'verbs_selected': 'Selected',
            'verbs_search': 'Search',
            'verbs_search_placeholder': 'Search verbs...',
            'verbs_select_header': 'Select',
            'verbs_row_header': 'Row',
            'verbs_infinitive_header': 'Infinitive',
            'verbs_past_simple_header': 'Past Simple',
            'verbs_past_participle_header': 'Past Participle',
            'verbs_spanish_header': 'Spanish Translation',
            'verbs_start_quiz': 'Start Quiz with Selected Verbs',
            'verbs_quick_load': 'Quick Load',
            'verbs_load': 'Load',

            # Study page
            'study_title': 'Quiz Mode',
            'study_info': 'Select verbs to start a quiz',
            'study_progress': 'Question',
            'study_of': 'of',
            'study_check': 'Check Answers',
            'study_next': 'Next Verb',
            'study_repeat': 'Repeat Quiz',
            'study_finish': 'Finish Quiz',
            'study_enter': 'Enter answer...',
            'study_infinitive': 'Infinitive',
            'study_past_simple': 'Past Simple',
            'study_past_participle': 'Past Participle',
            'study_spanish': 'Spanish Translation',

            # Statistics page
            'stats_title': 'Statistics',
            'stats_total_questions': 'Total Questions',
            'stats_total_correct': 'Total Correct',
            'stats_total_incorrect': 'Total Incorrect',
            'stats_accuracy': 'Overall Accuracy',
            'stats_session_history': 'Session History',
            'stats_date': 'Date',
            'stats_questions': 'Questions',
            'stats_correct': 'Correct',
            'stats_incorrect': 'Incorrect',
            'stats_accuracy_header': 'Accuracy',
            'stats_reset': 'Reset All Statistics',

            # Settings page
            'settings_title': 'Settings',
            'settings_theme': 'Theme',
            'settings_version': 'Version',
            'settings_save': 'Save Settings',
            'settings_saved': 'Settings Saved',
            'settings_saved_msg': 'Settings have been saved successfully.',
            'settings_error': 'Error',
            'settings_error_msg': 'Failed to save settings.',
            'settings_language': 'Language',

            # About page
            'about_title': 'About IrrVerEnglish',
            'about_app_name': 'Application Name',
            'about_version': 'Version',
            'about_description': 'Description',
            'about_desc_text': 'Desktop application for learning and practising English irregular verbs.',
            'about_creator': 'Creator',
            'about_release': 'Release',
            'about_release_text': 'Initial release, v1.0.0',

            # Messages
            'msg_no_selection': 'No Selection',
            'msg_no_selection_text': 'Please select at least one verb to start a quiz.',
            'msg_no_verbs': 'No Verbs',
            'msg_no_verbs_text': 'No verbs loaded to select from.',
            'msg_import_success': 'Import Successful',
            'msg_import_success_text': 'Successfully imported',
            'msg_import_error': 'Import Failed',
            'msg_import_error_text': 'No valid verbs could be imported from the file.',
            'msg_quiz_complete': 'Quiz Complete',
            'msg_quiz_results': 'Quiz Results',
            'msg_stats_reset': 'Statistics Reset',
            'msg_stats_reset_text': 'All statistics have been reset.',
            'msg_stats_confirm': 'Reset Statistics',
            'msg_stats_confirm_text': 'Are you sure you want to reset all statistics? This action cannot be undone.',
            'msg_range_invalid': 'Invalid Range',
            'msg_range_invalid_text': 'Start row must be less than or equal to end row.',
            'msg_range_title': 'Select by Row Range',
            'msg_range_start': 'Start Row',
            'msg_range_end': 'End Row',
        },
        'es': {
            # Navigation
            'nav_home': 'Inicio',
            'nav_study': 'Estudio',
            'nav_verbs': 'Verbos',
            'nav_statistics': 'Estadísticas',
            'nav_settings': 'Configuración',
            'nav_about': 'Acerca de',

            # Home page
            'home_welcome': 'Bienvenido a IrrVerEnglish',
            'home_description': 'Aprende y practica verbos irregulares en inglés con cuestionarios interactivos.\nImporta tus propios archivos CSV y personaliza tu experiencia de aprendizaje.',
            'home_csv_file': 'Archivo CSV',
            'home_csv_not_loaded': 'No cargado',
            'home_csv_loaded': 'Cargado',
            'home_available_verbs': 'Verbos Disponibles',
            'home_creator': 'Creador',
            'home_quick_actions': 'Acciones Rápidas',
            'home_import_csv': 'Importar CSV',
            'home_start_quiz': 'Iniciar Cuestionario',
            'home_view_verbs': 'Ver Verbos',

            # Verbs page
            'verbs_title': 'Gestión de Verbos',
            'verbs_import': 'Importar Archivo CSV',
            'verbs_loaded': 'Cargado',
            'verbs_verbs': 'verbos',
            'verbs_select_all': 'Seleccionar Todo',
            'verbs_deselect_all': 'Deseleccionar Todo',
            'verbs_invert': 'Invertir Selección',
            'verbs_range': 'Seleccionar por Rango de Filas',
            'verbs_selected': 'Seleccionados',
            'verbs_search': 'Buscar',
            'verbs_search_placeholder': 'Buscar verbos...',
            'verbs_select_header': 'Seleccionar',
            'verbs_row_header': 'Fila',
            'verbs_infinitive_header': 'Infinitivo',
            'verbs_past_simple_header': 'Pasado Simple',
            'verbs_past_participle_header': 'Participio Pasado',
            'verbs_spanish_header': 'Traducción Español',
            'verbs_start_quiz': 'Iniciar Cuestionario con Verbos Seleccionados',
            'verbs_quick_load': 'Carga Rápida',
            'verbs_load': 'Cargar',

            # Study page - Keep in English for learning
            'study_title': 'Quiz Mode',
            'study_info': 'Select verbs to start a quiz',
            'study_progress': 'Question',
            'study_of': 'of',
            'study_check': 'Check Answers',
            'study_next': 'Next Verb',
            'study_repeat': 'Repeat Quiz',
            'study_finish': 'Finish Quiz',
            'study_enter': 'Enter answer...',
            'study_infinitive': 'Infinitive',
            'study_past_simple': 'Past Simple',
            'study_past_participle': 'Past Participle',
            'study_spanish': 'Spanish Translation',

            # Statistics page
            'stats_title': 'Estadísticas',
            'stats_total_questions': 'Preguntas Totales',
            'stats_total_correct': 'Correctas Totales',
            'stats_total_incorrect': 'Incorrectas Totales',
            'stats_accuracy': 'Precisión General',
            'stats_session_history': 'Historial de Sesiones',
            'stats_date': 'Fecha',
            'stats_questions': 'Preguntas',
            'stats_correct': 'Correctas',
            'stats_incorrect': 'Incorrectas',
            'stats_accuracy_header': 'Precisión',
            'stats_reset': 'Reiniciar Todas las Estadísticas',

            # Settings page
            'settings_title': 'Configuración',
            'settings_theme': 'Tema',
            'settings_version': 'Versión',
            'settings_save': 'Guardar Configuración',
            'settings_saved': 'Configuración Guardada',
            'settings_saved_msg': 'La configuración se ha guardado exitosamente.',
            'settings_error': 'Error',
            'settings_error_msg': 'Error al guardar la configuración.',
            'settings_language': 'Idioma',

            # About page
            'about_title': 'Acerca de IrrVerEnglish',
            'about_app_name': 'Nombre de la Aplicación',
            'about_version': 'Versión',
            'about_description': 'Descripción',
            'about_desc_text': 'Aplicación de escritorio para aprender y practicar verbos irregulares en inglés.',
            'about_creator': 'Creador',
            'about_release': 'Lanzamiento',
            'about_release_text': 'Lanzamiento inicial, v1.0.0',

            # Messages
            'msg_no_selection': 'Sin Selección',
            'msg_no_selection_text': 'Por favor selecciona al menos un verbo para iniciar un cuestionario.',
            'msg_no_verbs': 'Sin Verbos',
            'msg_no_verbs_text': 'No hay verbos cargados para seleccionar.',
            'msg_import_success': 'Importación Exitosa',
            'msg_import_success_text': 'Importados exitosamente',
            'msg_import_error': 'Error de Importación',
            'msg_import_error_text': 'No se pudieron importar verbos válidos del archivo.',
            'msg_quiz_complete': 'Cuestionario Completado',
            'msg_quiz_results': 'Resultados del Cuestionario',
            'msg_stats_reset': 'Estadísticas Reiniciadas',
            'msg_stats_reset_text': 'Todas las estadísticas han sido reiniciadas.',
            'msg_stats_confirm': 'Reiniciar Estadísticas',
            'msg_stats_confirm_text': '¿Estás seguro de que quieres reiniciar todas las estadísticas? Esta acción no se puede deshacer.',
            'msg_range_invalid': 'Rango Inválido',
            'msg_range_invalid_text': 'La fila inicial debe ser menor o igual a la fila final.',
            'msg_range_title': 'Seleccionar por Rango de Filas',
            'msg_range_start': 'Fila Inicial',
            'msg_range_end': 'Fila Final',
        }
    }

    @staticmethod
    def get(key: str, language: str = 'en') -> str:
        """Get a translation for a key."""
        if language not in Translations.TRANSLATIONS:
            language = 'en'
        return Translations.TRANSLATIONS[language].get(key, key)

    @staticmethod
    def get_available_languages() -> list:
        """Get list of available languages."""
        return list(Translations.TRANSLATIONS.keys())

    @staticmethod
    def get_language_name(code: str) -> str:
        """Get human-readable language name."""
        names = {
            'en': 'English',
            'es': 'Español'
        }
        return names.get(code, code)
