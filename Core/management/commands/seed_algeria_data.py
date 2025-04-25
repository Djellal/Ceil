from django.core.management.base import BaseCommand
from Core.models import State, Municipality

class Command(BaseCommand):
    help = 'Seeds the database with Algerian states and municipalities'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding Algerian states and municipalities...')
        
        # Delete existing data to avoid duplicates
        Municipality.objects.all().delete()
        State.objects.all().delete()
        
        # Algerian states and their municipalities
        algeria_data = {
            'Adrar': {
                'name_ar': 'أدرار',
                'municipalities': [
                    {'name': 'Adrar', 'name_ar': 'أدرار'},
                    {'name': 'Reggane', 'name_ar': 'رقان'},
                    {'name': 'Timimoun', 'name_ar': 'تيميمون'},
                ]
            },
            'Chlef': {
                'name_ar': 'الشلف',
                'municipalities': [
                    {'name': 'Chlef', 'name_ar': 'الشلف'},
                    {'name': 'Ténès', 'name_ar': 'تنس'},
                    {'name': 'Boukadir', 'name_ar': 'بوقادير'},
                ]
            },
            'Laghouat': {
                'name_ar': 'الأغواط',
                'municipalities': [
                    {'name': 'Laghouat', 'name_ar': 'الأغواط'},
                    {'name': 'Aflou', 'name_ar': 'أفلو'},
                    {'name': 'Ksar El Hirane', 'name_ar': 'قصر الحيران'},
                ]
            },
            'Oum El Bouaghi': {
                'name_ar': 'أم البواقي',
                'municipalities': [
                    {'name': 'Oum El Bouaghi', 'name_ar': 'أم البواقي'},
                    {'name': 'Aïn Beïda', 'name_ar': 'عين البيضاء'},
                    {'name': 'Aïn M\'lila', 'name_ar': 'عين مليلة'},
                ]
            },
            'Batna': {
                'name_ar': 'باتنة',
                'municipalities': [
                    {'name': 'Batna', 'name_ar': 'باتنة'},
                    {'name': 'Barika', 'name_ar': 'بريكة'},
                    {'name': 'Arris', 'name_ar': 'أريس'},
                ]
            },
            'Béjaïa': {
                'name_ar': 'بجاية',
                'municipalities': [
                    {'name': 'Béjaïa', 'name_ar': 'بجاية'},
                    {'name': 'Akbou', 'name_ar': 'أقبو'},
                    {'name': 'Souk El Ténine', 'name_ar': 'سوق الإثنين'},
                ]
            },
            'Biskra': {
                'name_ar': 'بسكرة',
                'municipalities': [
                    {'name': 'Biskra', 'name_ar': 'بسكرة'},
                    {'name': 'Ouled Djellal', 'name_ar': 'أولاد جلال'},
                    {'name': 'Tolga', 'name_ar': 'طولقة'},
                ]
            },
            'Béchar': {
                'name_ar': 'بشار',
                'municipalities': [
                    {'name': 'Béchar', 'name_ar': 'بشار'},
                    {'name': 'Abadla', 'name_ar': 'العبادلة'},
                    {'name': 'Béni Abbès', 'name_ar': 'بني عباس'},
                ]
            },
            'Blida': {
                'name_ar': 'البليدة',
                'municipalities': [
                    {'name': 'Blida', 'name_ar': 'البليدة'},
                    {'name': 'Boufarik', 'name_ar': 'بوفاريك'},
                    {'name': 'Mouzaïa', 'name_ar': 'موزاية'},
                ]
            },
            'Bouira': {
                'name_ar': 'البويرة',
                'municipalities': [
                    {'name': 'Bouira', 'name_ar': 'البويرة'},
                    {'name': 'Lakhdaria', 'name_ar': 'الأخضرية'},
                    {'name': 'Sour El Ghozlane', 'name_ar': 'سور الغزلان'},
                ]
            },
            'Tamanrasset': {
                'name_ar': 'تمنراست',
                'municipalities': [
                    {'name': 'Tamanrasset', 'name_ar': 'تمنراست'},
                    {'name': 'In Salah', 'name_ar': 'عين صالح'},
                    {'name': 'In Guezzam', 'name_ar': 'عين قزام'},
                ]
            },
            'Tébessa': {
                'name_ar': 'تبسة',
                'municipalities': [
                    {'name': 'Tébessa', 'name_ar': 'تبسة'},
                    {'name': 'Bir el-Ater', 'name_ar': 'بئر العاتر'},
                    {'name': 'Cheria', 'name_ar': 'الشريعة'},
                ]
            },
            'Tlemcen': {
                'name_ar': 'تلمسان',
                'municipalities': [
                    {'name': 'Tlemcen', 'name_ar': 'تلمسان'},
                    {'name': 'Maghnia', 'name_ar': 'مغنية'},
                    {'name': 'Ghazaouet', 'name_ar': 'الغزوات'},
                ]
            },
            'Tiaret': {
                'name_ar': 'تيارت',
                'municipalities': [
                    {'name': 'Tiaret', 'name_ar': 'تيارت'},
                    {'name': 'Frenda', 'name_ar': 'فرندة'},
                    {'name': 'Ksar Chellala', 'name_ar': 'قصر الشلالة'},
                ]
            },
            'Tizi Ouzou': {
                'name_ar': 'تيزي وزو',
                'municipalities': [
                    {'name': 'Tizi Ouzou', 'name_ar': 'تيزي وزو'},
                    {'name': 'Azazga', 'name_ar': 'عزازقة'},
                    {'name': 'Draa El Mizan', 'name_ar': 'ذراع الميزان'},
                ]
            },
            'Alger': {
                'name_ar': 'الجزائر',
                'municipalities': [
                    {'name': 'Alger Centre', 'name_ar': 'الجزائر الوسطى'},
                    {'name': 'Bab El Oued', 'name_ar': 'باب الواد'},
                    {'name': 'Hussein Dey', 'name_ar': 'حسين داي'},
                    {'name': 'El Harrach', 'name_ar': 'الحراش'},
                    {'name': 'Bab Ezzouar', 'name_ar': 'باب الزوار'},
                ]
            },
            'Djelfa': {
                'name_ar': 'الجلفة',
                'municipalities': [
                    {'name': 'Djelfa', 'name_ar': 'الجلفة'},
                    {'name': 'Aïn Oussera', 'name_ar': 'عين وسارة'},
                    {'name': 'Messaad', 'name_ar': 'مسعد'},
                ]
            },
            'Jijel': {
                'name_ar': 'جيجل',
                'municipalities': [
                    {'name': 'Jijel', 'name_ar': 'جيجل'},
                    {'name': 'Taher', 'name_ar': 'الطاهير'},
                    {'name': 'El Milia', 'name_ar': 'الميلية'},
                ]
            },
            'Sétif': {
                'name_ar': 'سطيف',
                'municipalities': [
                    {'name': 'Sétif', 'name_ar': 'سطيف'},
                    {'name': 'El Eulma', 'name_ar': 'العلمة'},
                    {'name': 'Aïn Oulmene', 'name_ar': 'عين ولمان'},
                ]
            },
            'Saïda': {
                'name_ar': 'سعيدة',
                'municipalities': [
                    {'name': 'Saïda', 'name_ar': 'سعيدة'},
                    {'name': 'Youb', 'name_ar': 'يوب'},
                    {'name': 'Aïn El Hadjar', 'name_ar': 'عين الحجر'},
                ]
            },
            'Skikda': {
                'name_ar': 'سكيكدة',
                'municipalities': [
                    {'name': 'Skikda', 'name_ar': 'سكيكدة'},
                    {'name': 'Collo', 'name_ar': 'القل'},
                    {'name': 'Azzaba', 'name_ar': 'عزابة'},
                ]
            },
            'Sidi Bel Abbès': {
                'name_ar': 'سيدي بلعباس',
                'municipalities': [
                    {'name': 'Sidi Bel Abbès', 'name_ar': 'سيدي بلعباس'},
                    {'name': 'Telagh', 'name_ar': 'تلاغ'},
                    {'name': 'Sfisef', 'name_ar': 'سفيزف'},
                ]
            },
            'Annaba': {
                'name_ar': 'عنابة',
                'municipalities': [
                    {'name': 'Annaba', 'name_ar': 'عنابة'},
                    {'name': 'El Bouni', 'name_ar': 'البوني'},
                    {'name': 'Berrahal', 'name_ar': 'برحال'},
                ]
            },
            'Guelma': {
                'name_ar': 'قالمة',
                'municipalities': [
                    {'name': 'Guelma', 'name_ar': 'قالمة'},
                    {'name': 'Oued Zenati', 'name_ar': 'وادي الزناتي'},
                    {'name': 'Bouchegouf', 'name_ar': 'بوشقوف'},
                ]
            },
            'Constantine': {
                'name_ar': 'قسنطينة',
                'municipalities': [
                    {'name': 'Constantine', 'name_ar': 'قسنطينة'},
                    {'name': 'El Khroub', 'name_ar': 'الخروب'},
                    {'name': 'Hamma Bouziane', 'name_ar': 'حامة بوزيان'},
                ]
            },
            'Médéa': {
                'name_ar': 'المدية',
                'municipalities': [
                    {'name': 'Médéa', 'name_ar': 'المدية'},
                    {'name': 'Berrouaghia', 'name_ar': 'البرواقية'},
                    {'name': 'Ksar El Boukhari', 'name_ar': 'قصر البخاري'},
                ]
            },
            'Mostaganem': {
                'name_ar': 'مستغانم',
                'municipalities': [
                    {'name': 'Mostaganem', 'name_ar': 'مستغانم'},
                    {'name': 'Sidi Ali', 'name_ar': 'سيدي علي'},
                    {'name': 'Aïn Tedles', 'name_ar': 'عين تادلس'},
                ]
            },
            'M\'Sila': {
                'name_ar': 'المسيلة',
                'municipalities': [
                    {'name': 'M\'Sila', 'name_ar': 'المسيلة'},
                    {'name': 'Bou Saâda', 'name_ar': 'بوسعادة'},
                    {'name': 'Sidi Aïssa', 'name_ar': 'سيدي عيسى'},
                ]
            },
            'Mascara': {
                'name_ar': 'معسكر',
                'municipalities': [
                    {'name': 'Mascara', 'name_ar': 'معسكر'},
                    {'name': 'Sig', 'name_ar': 'سيق'},
                    {'name': 'Mohammadia', 'name_ar': 'المحمدية'},
                ]
            },
            'Ouargla': {
                'name_ar': 'ورقلة',
                'municipalities': [
                    {'name': 'Ouargla', 'name_ar': 'ورقلة'},
                    {'name': 'Hassi Messaoud', 'name_ar': 'حاسي مسعود'},
                    {'name': 'Touggourt', 'name_ar': 'تقرت'},
                ]
            },
            'Oran': {
                'name_ar': 'وهران',
                'municipalities': [
                    {'name': 'Oran', 'name_ar': 'وهران'},
                    {'name': 'Arzew', 'name_ar': 'أرزيو'},
                    {'name': 'Bir El Djir', 'name_ar': 'بئر الجير'},
                ]
            },
            'El Bayadh': {
                'name_ar': 'البيض',
                'municipalities': [
                    {'name': 'El Bayadh', 'name_ar': 'البيض'},
                    {'name': 'Labiodh Sidi Cheikh', 'name_ar': 'الأبيض سيدي الشيخ'},
                    {'name': 'Brezina', 'name_ar': 'بريزينة'},
                ]
            },
            'Illizi': {
                'name_ar': 'إليزي',
                'municipalities': [
                    {'name': 'Illizi', 'name_ar': 'إليزي'},
                    {'name': 'Djanet', 'name_ar': 'جانت'},
                    {'name': 'In Amenas', 'name_ar': 'عين أمناس'},
                ]
            },
            'Bordj Bou Arreridj': {
                'name_ar': 'برج بوعريريج',
                'municipalities': [
                    {'name': 'Bordj Bou Arreridj', 'name_ar': 'برج بوعريريج'},
                    {'name': 'Ras El Oued', 'name_ar': 'رأس الوادي'},
                    {'name': 'Mansourah', 'name_ar': 'المنصورة'},
                ]
            },
            'Boumerdès': {
                'name_ar': 'بومرداس',
                'municipalities': [
                    {'name': 'Boumerdès', 'name_ar': 'بومرداس'},
                    {'name': 'Bordj Menaïel', 'name_ar': 'برج منايل'},
                    {'name': 'Dellys', 'name_ar': 'دلس'},
                ]
            },
            'El Tarf': {
                'name_ar': 'الطارف',
                'municipalities': [
                    {'name': 'El Tarf', 'name_ar': 'الطارف'},
                    {'name': 'El Kala', 'name_ar': 'القالة'},
                    {'name': 'Ben M\'Hidi', 'name_ar': 'بن مهيدي'},
                ]
            },
            'Tindouf': {
                'name_ar': 'تندوف',
                'municipalities': [
                    {'name': 'Tindouf', 'name_ar': 'تندوف'},
                    {'name': 'Oum El Assel', 'name_ar': 'أم العسل'},
                ]
            },
            'Tissemsilt': {
                'name_ar': 'تيسمسيلت',
                'municipalities': [
                    {'name': 'Tissemsilt', 'name_ar': 'تيسمسيلت'},
                    {'name': 'Theniet El Had', 'name_ar': 'ثنية الحد'},
                    {'name': 'Bordj Bou Naama', 'name_ar': 'برج بونعامة'},
                ]
            },
            'El Oued': {
                'name_ar': 'الوادي',
                'municipalities': [
                    {'name': 'El Oued', 'name_ar': 'الوادي'},
                    {'name': 'Djamaa', 'name_ar': 'جامعة'},
                    {'name': 'Debila', 'name_ar': 'الدبيلة'},
                ]
            },
            'Khenchela': {
                'name_ar': 'خنشلة',
                'municipalities': [
                    {'name': 'Khenchela', 'name_ar': 'خنشلة'},
                    {'name': 'Kais', 'name_ar': 'قايس'},
                    {'name': 'Chechar', 'name_ar': 'ششار'},
                ]
            },
            'Souk Ahras': {
                'name_ar': 'سوق أهراس',
                'municipalities': [
                    {'name': 'Souk Ahras', 'name_ar': 'سوق أهراس'},
                    {'name': 'Sedrata', 'name_ar': 'سدراتة'},
                    {'name': 'Mechroha', 'name_ar': 'المشروحة'},
                ]
            },
            'Tipaza': {
                'name_ar': 'تيبازة',
                'municipalities': [
                    {'name': 'Tipaza', 'name_ar': 'تيبازة'},
                    {'name': 'Cherchell', 'name_ar': 'شرشال'},
                    {'name': 'Hadjout', 'name_ar': 'حجوط'},
                ]
            },
            'Mila': {
                'name_ar': 'ميلة',
                'municipalities': [
                    {'name': 'Mila', 'name_ar': 'ميلة'},
                    {'name': 'Chelghoum Laid', 'name_ar': 'شلغوم العيد'},
                    {'name': 'Ferdjioua', 'name_ar': 'فرجيوة'},
                ]
            },
            'Aïn Defla': {
                'name_ar': 'عين الدفلى',
                'municipalities': [
                    {'name': 'Aïn Defla', 'name_ar': 'عين الدفلى'},
                    {'name': 'Khemis Miliana', 'name_ar': 'خميس مليانة'},
                    {'name': 'Miliana', 'name_ar': 'مليانة'},
                ]
            },
            'Naâma': {
                'name_ar': 'النعامة',
                'municipalities': [
                    {'name': 'Naâma', 'name_ar': 'النعامة'},
                    {'name': 'Mécheria', 'name_ar': 'المشرية'},
                    {'name': 'Aïn Sefra', 'name_ar': 'عين الصفراء'},
                ]
            },
            'Aïn Témouchent': {
                'name_ar': 'عين تموشنت',
                'municipalities': [
                    {'name': 'Aïn Témouchent', 'name_ar': 'عين تموشنت'},
                    {'name': 'Hammam Bouhadjar', 'name_ar': 'حمام بوحجر'},
                    {'name': 'Beni Saf', 'name_ar': 'بني صاف'},
                ]
            },
            'Ghardaïa': {
                'name_ar': 'غرداية',
                'municipalities': [
                    {'name': 'Ghardaïa', 'name_ar': 'غرداية'},
                    {'name': 'Metlili', 'name_ar': 'متليلي'},
                    {'name': 'El Guerrara', 'name_ar': 'القرارة'},
                ]
            },
            'Relizane': {
                'name_ar': 'غليزان',
                'municipalities': [
                    {'name': 'Relizane', 'name_ar': 'غليزان'},
                    {'name': 'Oued Rhiou', 'name_ar': 'وادي رهيو'},
                    {'name': 'Mazouna', 'name_ar': 'مازونة'},
                ]
            },
        }
        
        # Create states and municipalities
        for state_name, state_data in algeria_data.items():
            state = State.objects.create(
                name=state_name,
                name_ar=state_data['name_ar']
            )
            
            for muni_data in state_data['municipalities']:
                Municipality.objects.create(
                    name=muni_data['name'],
                    name_ar=muni_data['name_ar'],
                    state=state
                )
        
        self.stdout.write(self.style.SUCCESS(f'Successfully seeded {State.objects.count()} states and {Municipality.objects.count()} municipalities'))