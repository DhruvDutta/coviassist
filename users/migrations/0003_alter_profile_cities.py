# Generated by Django 3.2.2 on 2021-05-06 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210506_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='cities',
            field=models.CharField(blank=True, choices=[('Delhi', 'Delhi'), ('Kolkata', 'Kolkata'), ('Mumbai', 'Mumbai'), ('Hyderabad', 'Hyderabad'), ('Bengaluru', 'Bengaluru'), ('Chennai', 'Chennai'), ('Ahmedabad', 'Ahmedabad'), ('Surat', 'Surat'), ('Pune', 'Pune'), ('Jaipur', 'Jaipur'), ('Kanpur', 'Kanpur'), ('Lucknow', 'Lucknow'), ('Nagpur', 'Nagpur'), ('Ghaziabad', 'Ghaziabad'), ('Indore', 'Indore'), ('Coimbatore', 'Coimbatore'), ('Patna', 'Patna'), ('Visakhapatnam', 'Visakhapatnam'), ('Bhopal', 'Bhopal'), ('Nashik', 'Nashik'), ('Pimpri-Chinchwad', 'Pimpri-Chinchwad'), ('Agra', 'Agra'), ('Vadodara', 'Vadodara'), ('Ludhiana', 'Ludhiana'), ('Madurai', 'Madurai'), ('Varanasi', 'Varanasi'), ('Meerut', 'Meerut'), ('Faridabad', 'Faridabad'), ('Jamshedpur', 'Jamshedpur'), ('Rajkot', 'Rajkot'), ('Jabalpur', 'Jabalpur'), ('Asansol', 'Asansol'), ('Allahabad', 'Allahabad'), ('Dhanbad', 'Dhanbad'), ('Srinagar', 'Srinagar'), ('Aurangabad', 'Aurangabad'), ('Jodhpur', 'Jodhpur'), ('Amritsar', 'Amritsar'), ('Ranchi', 'Ranchi'), ('Gwalior', 'Gwalior'), ('Chandigarh', 'Chandigarh'), ('Vijayawada', 'Vijayawada'), ('Tiruchirappalli', 'Tiruchirappalli'), ('Raipur', 'Raipur'), ('Kota', 'Kota'), ('Bareilly', 'Bareilly'), ('Guwahati', 'Guwahati'), ('Tirupur', 'Tirupur'), ('Thiruvananthapuram', 'Thiruvananthapuram'), ('Solapur', 'Solapur'), ('Hubli', 'Hubli'), ('Salem', 'Salem'), ('Aligarh', 'Aligarh'), ('Gurgaon', 'Gurgaon'), ('Durg', 'Durg'), ('Moradabad', 'Moradabad'), ('Mysore', 'Mysore'), ('Bhubaneswar', 'Bhubaneswar'), ('Jalandhar', 'Jalandhar'), ('Warangal', 'Warangal'), ('Guntur', 'Guntur'), ('Dehradun', 'Dehradun'), ('Bhiwandi', 'Bhiwandi'), ('Saharanpur', 'Saharanpur'), ('Siliguri', 'Siliguri'), ('Gorakhpur', 'Gorakhpur'), ('Cuttack', 'Cuttack'), ('Pondicherry', 'Pondicherry'), ('Amravati', 'Amravati'), ('Bikaner', 'Bikaner'), ('Faizabad', 'Faizabad'), ('Kochi', 'Kochi'), ('Firozabad', 'Firozabad'), ('Bhavnagar', 'Bhavnagar'), ('Durgapur', 'Durgapur'), ('Bokaro Steel City', 'Bokaro Steel City'), ('Naya Raipur', 'Naya Raipur'), ('Rourkela', 'Rourkela'), ('Ajmer', 'Ajmer'), ('Nanded', 'Nanded'), ('Kolhapur', 'Kolhapur'), ('Jhansi', 'Jhansi'), ('Gulbarga', 'Gulbarga'), ('Agartala', 'Agartala'), ('Erode', 'Erode'), ('Ujjain', 'Ujjain'), ('Sangli-Miraj-Kupwad', 'Sangli-Miraj-Kupwad'), ('Jammu', 'Jammu'), ('Nellore', 'Nellore'), ('Mangalore', 'Mangalore'), ('Tirunelveli', 'Tirunelveli'), ('Muzaffarnagar', 'Muzaffarnagar'), ('Belgaum', 'Belgaum'), ('Vellore', 'Vellore'), ('Jamnagar', 'Jamnagar'), ('Udaipur', 'Udaipur'), ('Gaya', 'Gaya'), ('Jalgaon', 'Jalgaon'), ('Mathura', 'Mathura'), ('Patiala', 'Patiala'), ('Panipat', 'Panipat'), ('Davangere', 'Davangere'), ('Calicut', 'Calicut'), ('Akola', 'Akola'), ('Kurnool', 'Kurnool'), ('Rajamahendravaram', 'Rajamahendravaram'), ('Latur', 'Latur'), ('Tuticorin', 'Tuticorin'), ('Bhagalpur', 'Bhagalpur'), ('Malegaon', 'Malegaon'), ('Bellary', 'Bellary'), ('Ambala', 'Ambala'), ('Muzaffarpur', 'Muzaffarpur'), ('Yamunanagar', 'Yamunanagar'), ('Dhule', 'Dhule'), ('Dimapur', 'Dimapur'), ('Tirupati', 'Tirupati'), ('Rohtak', 'Rohtak'), ('Sagar', 'Sagar'), ('Budaun', 'Budaun'), ('Korba', 'Korba'), ('Bhilwara', 'Bhilwara'), ('Rampur', 'Rampur'), ('Shahjahanpur', 'Shahjahanpur'), ('Berhampur', 'Berhampur'), ('Ahmednagar', 'Ahmednagar'), ('Kollam', 'Kollam'), ('Bardhaman', 'Bardhaman'), ('Kadapa', 'Kadapa'), ('Alwar', 'Alwar'), ('Bilaspur', 'Bilaspur'), ('Nandurbar', 'Nandurbar'), ('Bijapur', 'Bijapur'), ('Ichalkaranji', 'Ichalkaranji'), ('Thrissur', 'Thrissur'), ('Chandrapur', 'Chandrapur'), ('Malda', 'Malda'), ('Shimoga', 'Shimoga'), ('Junagadh', 'Junagadh'), ('Farrukhabad', 'Farrukhabad'), ('Kakinada', 'Kakinada'), ('Nizamabad', 'Nizamabad'), ('Purnia', 'Purnia'), ('Haridwar', 'Haridwar'), ('Hisar', 'Hisar'), ('Darbhanga', 'Darbhanga'), ('Tumkur', 'Tumkur'), ('Baharampur', 'Baharampur'), ('Habra', 'Habra'), ('Jalpaiguri', 'Jalpaiguri'), ('Karnal', 'Karnal'), ('Ozhukarai', 'Ozhukarai'), ('Bihar Sharif', 'Bihar Sharif'), ('Kharagpur', 'Kharagpur'), ('Aizawl', 'Aizawl'), ('Sonipat', 'Sonipat'), ('Gudiyatham', 'Gudiyatham'), ('Dewas', 'Dewas'), ('Shantipur', 'Shantipur'), ('Bathinda', 'Bathinda'), ('Jalna', 'Jalna'), ('Satna', 'Satna'), ('Mau', 'Mau'), ('Roorkee', 'Roorkee'), ('Ratlam', 'Ratlam'), ('Parbhani', 'Parbhani'), ('Sambalpur', 'Sambalpur'), ('Anantapur', 'Anantapur'), ('Imphal', 'Imphal'), ('Rajnandgaon', 'Rajnandgaon'), ('Hapur', 'Hapur'), ('Karimnagar', 'Karimnagar'), ('Arrah', 'Arrah'), ('Noida', 'Noida'), ('Etawah', 'Etawah'), ('Haldwani', 'Haldwani'), ('Bharatpur', 'Bharatpur'), ('Begusarai', 'Begusarai'), ('Sri Ganganagar', 'Sri Ganganagar'), ('Dankuni', 'Dankuni'), ('Gandhidham', 'Gandhidham'), ('Mirzapur', 'Mirzapur'), ('Sikar', 'Sikar'), ('Katihar', 'Katihar'), ('Dhulian', 'Dhulian'), ('Ranaghat', 'Ranaghat'), ('Rewa', 'Rewa'), ('Bulandshahr', 'Bulandshahr'), ('Kannur', 'Kannur'), ('Raichur', 'Raichur'), ('Pali', 'Pali'), ('Ramagundam', 'Ramagundam'), ('Silchar', 'Silchar'), ('Vizianagaram', 'Vizianagaram'), ('Nagercoil', 'Nagercoil'), ('Thanjavur', 'Thanjavur'), ('Katni', 'Katni'), ('Sambhal', 'Sambhal'), ('Singrauli', 'Singrauli'), ('Nadiad', 'Nadiad'), ('Eluru', 'Eluru'), ('Bidar', 'Bidar'), ('Munger', 'Munger'), ('Chhapra', 'Chhapra'), ('Burhanpur', 'Burhanpur'), ('Panchkula', 'Panchkula'), ('Dindigul', 'Dindigul'), ('Gandhinagar', 'Gandhinagar'), ('Hospet', 'Hospet'), ('Bhusawal', 'Bhusawal'), ('Deoghar', 'Deoghar'), ('Ongole', 'Ongole'), ('Puri', 'Puri'), ('Haldia', 'Haldia'), ('Nandyal', 'Nandyal'), ('Khandwa', 'Khandwa'), ('Morena', 'Morena'), ('Raiganj', 'Raiganj'), ('Anand', 'Anand'), ('Bhiwani', 'Bhiwani'), ('Bhind', 'Bhind'), ('Amroha', 'Amroha'), ('Hardoi', 'Hardoi'), ('Vaniyambadi', 'Vaniyambadi'), ('Morbi', 'Morbi'), ('Fatehpur', 'Fatehpur'), ('Kasaragod', 'Kasaragod'), ('Raebareli', 'Raebareli'), ('Daman', 'Daman'), ('Orai', 'Orai'), ('Chhindwara', 'Chhindwara'), ('Barmer', 'Barmer'), ('Sitapur', 'Sitapur'), ('Bahraich', 'Bahraich'), ('Phusro', 'Phusro'), ('Khammam', 'Khammam'), ('Khambhat', 'Khambhat'), ('Sirsa', 'Sirsa'), ('Modinagar', 'Modinagar'), ('Krishnanagar', 'Krishnanagar'), ('Guna', 'Guna'), ('Shivpuri', 'Shivpuri'), ('Unnao', 'Unnao'), ('Surendranagar', 'Surendranagar'), ('Balasore', 'Balasore'), ('Nabadwip', 'Nabadwip'), ('Bongaigaon', 'Bongaigaon'), ('Alappuzha', 'Alappuzha'), ('Alappuzha', 'Alappuzha'), ('Cuddalore', 'Cuddalore'), ('Hassan', 'Hassan'), ('Gadag', 'Gadag'), ('Shimla', 'Shimla'), ('Komarapalayam', 'Komarapalayam'), ('Bahadurgarh', 'Bahadurgarh'), ('Machilipatnam', 'Machilipatnam'), ('Midnapore', 'Midnapore'), ('Bharuch', 'Bharuch'), ('Hoshiarpur', 'Hoshiarpur'), ('Jaunpur', 'Jaunpur'), ('Adoni', 'Adoni'), ('Jind', 'Jind'), ('Udupi', 'Udupi'), ('Tonk', 'Tonk'), ('Tenali', 'Tenali'), ('Lakhimpur', 'Lakhimpur'), ('Balurghat', 'Balurghat'), ('Kanchipuram', 'Kanchipuram'), ('Vapi', 'Vapi'), ('Proddatur', 'Proddatur'), ('Ambur', 'Ambur'), ('Robertsonpet', 'Robertsonpet'), ('Hathras', 'Hathras'), ('Navsari', 'Navsari'), ('Banda', 'Banda'), ('Pilibhit', 'Pilibhit'), ('Mahbubnagar', 'Mahbubnagar'), ('Bettiah', 'Bettiah'), ('Vidisha', 'Vidisha'), ('Saharsa', 'Saharsa'), ('Kishangarh', 'Kishangarh'), ('Thanesar', 'Thanesar'), ('Barabanki', 'Barabanki'), ('Mughalsarai', 'Mughalsarai'), ('Veraval', 'Veraval'), ('Rudrapur', 'Rudrapur'), ('Chittorgarh', 'Chittorgarh'), ('Dibrugarh', 'Dibrugarh'), ('Chittoor', 'Chittoor'), ('Hazaribagh', 'Hazaribagh'), ('Jorhat', 'Jorhat'), ('Hindupur', 'Hindupur'), ('Porbandar', 'Porbandar'), ('Batala', 'Batala'), ('Beawar', 'Beawar'), ('Bhadravati', 'Bhadravati'), ('Hanumangarh', 'Hanumangarh'), ('Satara', 'Satara'), ('Chhatarpur', 'Chhatarpur'), ('Hajipur', 'Hajipur'), ('Damoh', 'Damoh'), ('Sasaram', 'Sasaram'), ('Nagaon', 'Nagaon'), ('Beed', 'Beed'), ('Mohali', 'Mohali'), ('Chitradurga', 'Chitradurga'), ('Tiruvannamalai', 'Tiruvannamalai'), ('Abohar', 'Abohar'), ('Harihar', 'Harihar'), ('Basirhat', 'Basirhat'), ('Kaithal', 'Kaithal'), ('Pudukkottai', 'Pudukkottai'), ('Godhra', 'Godhra'), ('Giridih', 'Giridih'), ('Pathankot', 'Pathankot'), ('Shillong', 'Shillong'), ('Bhuj', 'Bhuj'), ('Khurja', 'Khurja'), ('Bhimavaram', 'Bhimavaram'), ('Pakhanjore', 'Pakhanjore'), ('Mandsaur', 'Mandsaur'), ('Moga', 'Moga'), ('Rewari', 'Rewari'), ('Ankleshwar', 'Ankleshwar'), ('Kumbakonam', 'Kumbakonam'), ('Pandharpur', 'Pandharpur'), ('Gonda', 'Gonda'), ('Kolar', 'Kolar'), ('Yavatmal', 'Yavatmal'), ('Bankura', 'Bankura'), ('Mandya', 'Mandya'), ('Dehri', 'Dehri'), ('Kamptee', 'Kamptee'), ('Nalgonda', 'Nalgonda'), ('Madanapalle', 'Madanapalle'), ('Malerkotla', 'Malerkotla'), ('Siwan', 'Siwan'), ('Khargone', 'Khargone'), ('Mainpuri', 'Mainpuri'), ('Dholpur', 'Dholpur'), ('Lalitpur', 'Lalitpur'), ('Chakdaha', 'Chakdaha'), ('Gondia', 'Gondia'), ('Ramgarh', 'Ramgarh'), ('Darjeeling', 'Darjeeling'), ('Palwal', 'Palwal'), ('Etah', 'Etah'), ('Palakkad', 'Palakkad'), ('Rajapalayam', 'Rajapalayam'), ('Botad', 'Botad'), ('Gangapur', 'Gangapur'), ('Kottayam', 'Kottayam'), ('Deoria', 'Deoria'), ('Bhadrak', 'Bhadrak'), ('Neemuch', 'Neemuch'), ('Khanna', 'Khanna'), ('Alipurduar', 'Alipurduar'), ('Purulia', 'Purulia'), ('Guntakal', 'Guntakal'), ('Pithampur', 'Pithampur'), ('Ujhani', 'Ujhani'), ('Srikakulam', 'Srikakulam'), ('Tinsukia', 'Tinsukia'), ('Patan', 'Patan'), ('Jagdalpur', 'Jagdalpur'), ('Motihari', 'Motihari'), ('Jangipur', 'Jangipur'), ('Palanpur', 'Palanpur'), ('Dharmavaram', 'Dharmavaram'), ('Kashipur', 'Kashipur'), ('Ghazipur', 'Ghazipur'), ('Sawai Madhopur', 'Sawai Madhopur'), ('Churu', 'Churu'), ('Medininagar', 'Medininagar'), ('Dahod', 'Dahod'), ('Chirkunda', 'Chirkunda'), ('Nawada', 'Nawada'), ('Chikkamagallooru', 'Chikkamagallooru'), ('Chikmagalur', 'Chikmagalur'), ('Jetpur', 'Jetpur'), ('Gudivada', 'Gudivada'), ('Baran', 'Baran'), ('Hoshangabad', 'Hoshangabad'), ('Adilabad', 'Adilabad'), ('Muktasar', 'Muktasar'), ('Baripada', 'Baripada'), ('Hosur', 'Hosur'), ('Barnala', 'Barnala'), ('Makrana', 'Makrana'), ('Narasaraopet', 'Narasaraopet'), ('Sultanpur', 'Sultanpur'), ('Azamgarh', 'Azamgarh'), ('Bijnor', 'Bijnor'), ('Sahaswan', 'Sahaswan'), ('Basti', 'Basti'), ('Gangawati', 'Gangawati'), ('Kothamangalam', 'Kothamangalam'), ('Valsad', 'Valsad'), ('Ambikapur', 'Ambikapur'), ('Itarsi', 'Itarsi'), ('Panaji', 'Panaji'), ('Chandausi', 'Chandausi'), ('Siddipet', 'Siddipet'), ('Kalol', 'Kalol'), ('Bagaha', 'Bagaha'), ('Achalpur', 'Achalpur'), ('Gondal', 'Gondal'), ('Osmanabad', 'Osmanabad'), ('Akbarpur', 'Akbarpur'), ('Ballia', 'Ballia'), ('Deesa', 'Deesa'), ('Nagaur', 'Nagaur'), ('Bangaon', 'Bangaon'), ('Buxar', 'Buxar'), ('Firozpur', 'Firozpur'), ('Hindaun', 'Hindaun'), ('Mubarakpur', 'Mubarakpur'), ('Tanda', 'Tanda'), ('Dhubri', 'Dhubri'), ('Sehore', 'Sehore'), ('Anantnag', 'Anantnag'), ('Tadipatri', 'Tadipatri'), ('Port Blair', 'Port Blair'), ('Greater Noida', 'Greater Noida'), ('Shikohabad', 'Shikohabad'), ('Shamli', 'Shamli'), ('Kishanganj', 'Kishanganj'), ('Hinganghat', 'Hinganghat'), ('Cooch Behar', 'Cooch Behar'), ('Karaikudi', 'Karaikudi'), ('Wardha', 'Wardha'), ('Ranebennuru', 'Ranebennuru'), ('Sitamarhi', 'Sitamarhi'), ('Neyveli', 'Neyveli'), ('Amreli', 'Amreli'), ('Amreli', 'Amreli'), ('Suryapet', 'Suryapet'), ('Jamalpur', 'Jamalpur'), ('Bhiwadi', 'Bhiwadi'), ('Barshi', 'Barshi'), ('Bundi', 'Bundi'), ('Tadepalligudem', 'Tadepalligudem'), ('Miryalaguda', 'Miryalaguda'), ('Chirmiri', 'Chirmiri'), ('Betul', 'Betul'), ('Amaravati', 'Amaravati'), ('Nagapattinam', 'Nagapattinam'), ('Baraut', 'Baraut'), ('Jehanabad', 'Jehanabad'), ('Seoni', 'Seoni'), ('Rishikesh', 'Rishikesh'), ('Khair', 'Khair'), ('Dhamtari', 'Dhamtari'), ('Kapurthala', 'Kapurthala'), ('Sujangarh', 'Sujangarh'), ('Aurangabad', 'Aurangabad'), ('Chilakaluripet', 'Chilakaluripet'), ('Malappuram', 'Malappuram'), ('Kasganj', 'Kasganj'), ('Vasco', 'Vasco'), ('Tezpur', 'Tezpur'), ('Jhunjhunu', 'Jhunjhunu'), ('Datia', 'Datia'), ('Banswara', 'Banswara'), ('Raigarh', 'Raigarh'), ('Nagda', 'Nagda'), ('Lakhisarai', 'Lakhisarai'), ('Auraiya', 'Auraiya'), ('Kohima', 'Kohima'), ('Gangtok', 'Gangtok'), ('Mahuva', 'Mahuva'), ('Silvassa', 'Silvassa'), ('Balangir', 'Balangir'), ('Phagwara', 'Phagwara'), ('Jharsuguda', 'Jharsuguda'), ('Chalisgaon', 'Chalisgaon'), ('Khatauli', 'Khatauli'), ('Manjeri', 'Manjeri'), ('Mormugao', 'Mormugao'), ('Deoband', 'Deoband'), ('Mahasamund', 'Mahasamund'), ('Jagtial', 'Jagtial'), ('Viluppuram', 'Viluppuram'), ('Amalner', 'Amalner'), ('Sardarshahar', 'Sardarshahar'), ('Paramakudi', 'Paramakudi'), ('Zirakpur', 'Zirakpur'), ('Tiruchengode', 'Tiruchengode'), ('Nagina', 'Nagina'), ('Mahoba', 'Mahoba'), ('Muradnagar', 'Muradnagar'), ('Ramanagara', 'Ramanagara'), ('Kovilpatti', 'Kovilpatti'), ('Dhanpuri', 'Dhanpuri'), ('Bhadohi', 'Bhadohi'), ('Theni-Allinagaram', 'Theni-Allinagaram'), ('Khamgaon', 'Khamgaon'), ('Dhar', 'Dhar'), ('Balaghat', 'Balaghat'), ('Akot', 'Akot'), ('Fatehpur', 'Fatehpur'), ('Thalassery', 'Thalassery'), ('Bolpur', 'Bolpur'), ('Kanthi', 'Kanthi'), ('Rajpura', 'Rajpura'), ('Udgir', 'Udgir'), ('Bhandara', 'Bhandara'), ('Dadri', 'Dadri'), ('Ponnani', 'Ponnani'), ('Kadayanallur', 'Kadayanallur'), ('Pratapgarh', 'Pratapgarh'), ('Pollachi', 'Pollachi'), ('Najibabad', 'Najibabad'), ('Parli', 'Parli'), ('Ooty', 'Ooty'), ('Jhumri Telaiya', 'Jhumri Telaiya'), ('Margao', 'Margao'), ('Mancherial', 'Mancherial'), ('Karaikal', 'Karaikal'), ('Dausa', 'Dausa'), ('Jeypore', 'Jeypore'), ('Mehsana', 'Mehsana'), ('Karauli', 'Karauli'), ('Sahibganj', 'Sahibganj'), ('Kothagudem', 'Kothagudem'), ('Itanagar', 'Itanagar'), ('Bagalkot', 'Bagalkot'), ('Kavaratti', 'Kavaratti')], max_length=50),
        ),
    ]