const newsData = [
    {
        imageSrc: '/images/news/news_54/news54.jpeg',
        title: 'III სადირექციო წერის საკითხები (მათემატიკა)',
        date: '27 მარტი, 2024',
        description: 'ანდრია რაზმაძის სახელობის N41 ფიზიკა-მათემატიკის საჯარო სკოლის N3 სადირექციო წერის ნიმუშები',
        link: '/News_Feed/news_54.html',
    },
    {
        imageSrc: '/images/news/news_53/news_53.jpg',
        title: '"თიბისის განათლების სივრცე"',
        date: '17 მარტი, 2024',
        description: 'თიბისიმ ახალი თაობისთვის ახალი პროექტი, "თიბისის განათლების სივრცე" შექმნა. პროექტის ფარგლებში,  ... ',
        link: '/News_Feed/news_53.html',
    },
    {
        imageSrc: '/images/news/news_52/news52.jpg',
        title: 'ანა სალდაძე FLEX-ის გამარჯვებული გახდა!',
        date: '17 მარტი, 2024',
        description: 'ანდრია რაზმაძის სახელობის ქუთაისის N41 ფიზიკა-მათემატიკის საჯარო სკოლის ... ',
        link: '/News_Feed/news_52.html',
    },
    {
        imageSrc: '/images/news/news_51/news51.jpg',
        title: 'III სადირექციო წერის განრიგი',
        date: '5 მარტი, 2024',
        description: ' ანდრია რაზმაძის სახელობის ქალაქ ქუთაისის N41 ფიზიკა-მათემატიკის საჯარო   ... ',
        link: '/News_Feed/news_51.html',
    },
    {
        imageSrc: '/images/news/news_50/news50.jpg',
        title: ' საერთაშორისო ახალგაზრდული ოლიმპიადა ინფორმატიკაში',
        date: '5 მარტი, 2024',
        description: '2024 წლის 9-11 თებერვალს რუმინეთში გაიმართა საერთაშორისო ახალგაზრდული  ... ',
        link: '/News_Feed/news_50.html',
    },
    {
        imageSrc: '/images/news/news_49/news49.jpg',
        title: ' ჟაუტიკოვის ოლიმპიადაში გამარჯვებულებს მედლები გადაეცათ',
        date: '5 მარტი, 2024',
        description: 'ანდრია რაზმაძის სახელობის ქუთაისის N41 ფიზიკა-მათემატიკის საჯარო სკოლის 2021 ... ',
        link: '/News_Feed/news_49.html',
    },
    {
        imageSrc: '/images/news/news_48/news48.jpg',
        title: ' მოსწავლეებს ოქროსა და ვერცხლის მედლები გადაეცათ',
        date: '5 მარტი, 2024',
        description: '  ანდრია რაზმაძის სახელობის ქუთაისის N41 ფიზიკა-მათემატიკის საჯარო სკოლის ... ',
        link: '/News_Feed/news_48.html',
    },
    {
        imageSrc: '/images/news/news_47/news47.jpg',
        title: ' ბარბარე კუჭავა Egmo-ს ნაკრებშია',
        date: '5 მარტი, 2024',
        description: '  2024 წელს საქართველო ევროპის გოგონათა მათემატიკის - EGMO რიგით მეცამეტე ოლიმპიადას... ',
        link: '/News_Feed/news_47.html',
    },
    {
        imageSrc: '/images/news/news_46/news46.jpg',
        title: ' 1000 ლარი მოსწავლეებს ქუთაისის მერისგან',
        date: '5 მარტი, 2024',
        description: '  დღეს, 15 თებერვალს ქუთაისის მერის იოსებ ხახალეიშვილის ინიციატივით... ',
        link: '/News_Feed/news_46.html',
    },
    {
        imageSrc: '/images/news/news_45/news45.jpg',
        title: ' პროექტი ჭკვიანი ქალაქის შესახებ',
        date: '15 თებერვალი, 2024',
        description: '  პირველ სემესტრის დასასრულს დირექტორის პირველი მოადგილის ქალბატონ... ',
        link: '/News_Feed/news_45.html',
    },
    {
        imageSrc: '/images/news/news_44/news44.jpg',
        title: '"მაია ჩიბურდანიძის სახელობის" ჩემპიონატი',
        date: '12 თებერვალი, 2024',
        description: '  27 იანვარს ქუთაისის მაია ჩიბურდანიძის სახელობის ჭადრაკის სკოლაში გაიმართა',
        link: '/News_Feed/news_44.html',
    },
    {
        imageSrc: '/images/news/news_43/news43.jpg',
        title: '"ტვინების ბრძოლა"',
        date: '12 თებერვალი, 2024',
        description: ' გუნდურ-ინტელექტუალური თამაშის ,,ტვინების ბრძოლის" 2023 წლის შემოდგომის',
        link: '/News_Feed/news_43.html',
    },
    {
        imageSrc: '/images/additional_news/school_projects/school_project12/school_project12.jpg',
        title: 'პროექტი ოთარ თაქთაქიშვილზე',
        date: '31 იანვარი, 2024',
        description: 'მასწავლებელ ქეთევან მაღლაფერიძის ხელმძღვანელობით წარმოადგინეს პროექტი დიდი ქართველი ...',
        link: '/Projects_and_memoranda/school_projects/school_project_12.html',
    },
    {
        imageSrc: '/images/additional_news/school_projects/school_project11/school_project11_2.jpg',
        title: 'ცენტრალური სამუსიკო სასწავლებელი',
        date: '31 იანვარი, 2024',
        description: '2024 წლის 18 იანვარს მელიტონ ბალანჩივაძის სახელობის ცენტრალური სამუსიკო ...',
        link: '/Projects_and_memoranda/school_projects/school_project_11.html',
    },
    {
        imageSrc: '/images/news/news_42/news42.jpg',
        title: 'საერთაშორისო ოლიმპიადა (IZhO) მოსწავლეებისთვის',
        date: '31 იანვარი, 2024',
        description: 'ყაზახეთის რესპუბლიკაში ქალაქ ალმატიში 7-14 იანვარს ჩატარებულ ჟაუტიკოვის XX საერთაშორისო ოლიმპიადაზე',
        link: '/News_Feed/news_42.html',
    },
    {
        imageSrc: '/images/news/news_41/news41.jpg',
        title: 'საერთაშორისო ოლიმპიადა (IMPACT) მასწავლებლებისთვის',
        date: '31 იანვარი, 2024',
        description: 'ყაზახეთის რესპუბლიკაში ქალაქ ალმატიში 7-14 იანვარს ჩატარებულ IMPACT საერთაშორისო ოლიმპიადაზე',
        link: '/News_Feed/news_41.html',
    },
    {
        imageSrc: '/images/news/news_40/news40.jpeg',
        title: 'II სადირექციო წერის ნიმუშები (ფიზიკა)',
        date: '31 დეკემბერი, 2023',
        description: 'ანდრია რაზმაძის სახელობის N41 ფიზიკა-მათემატიკის საჯარო სკოლის N2 სადირექციო წერის ნიმუშები',
        link: '/News_Feed/news_40.html',
    },
    {
        imageSrc: '/images/news/news_39/news39.jpeg',
        title: ' საერთაშორისო ოლიმპიადა (IZhO) მათემატიკაში',
        date: '31 დეკემბერი, 2023',
        description: 'ყაზახეთის ქალაქ ალმათიში 2024 წლის 8-13 იანვარს იმართება ჟაუტიკოვის ოლიმპიადა (IZhO) მათემატიკაში...',
        link: 'News_Feed/news_39.html',
    },
    {
        imageSrc: '/images/news/news_38/news38_1.jpg',
        title: 'საახალწლო საქველმოქმედო აქცია',
        date: '31 დეკემბერი, 2023',
        description: 'სკოლის V კლასის მოსწავლეები და მასწავლებლები ეწვივნენ ქუთაისის ხანდაზმულთა პანსიონატს ...',
        link: 'News_Feed/news_38.html',
    },
    {
        imageSrc: '/images/news/news_37/news37.jpg',
        title: 'საახალწლო საქველმოქმედო აქცია',
        date: '31 დეკემბერი, 2023',
        description: 'სკოლის მოსწავლეები და მასწავლებლები ეწვივნენ ქუთაისის ხანდაზმულთა პანსიონატს ...',
        link: 'News_Feed/news_37.html',
    },
    {
        imageSrc: '/images/news/news_36/news36_9.jpg',
        title: 'საახალწლო კარნავალი',
        date: '30 დეკემბერი, 2023',
        description: '2023 წლის 25-26 დეკემბერს სკოლაში სკოლის სამოქალაქო კლუბი ...',
        link: 'News_Feed/news_36.html',
    },
    {
        imageSrc: '/images/news/news_35/news35.jpg',
        title: '„რობოტების ბრძოლა - Sumo Challenge-ს“',
        date: '30 დეკემბერი, 2023',
        description: 'სკოლა აცხადებს „რობოტების ბრძოლა - Sumo Challenge“ ...',
        link: 'News_Feed/news_35.html',
    },
    {
        imageSrc: '/images/news/news_34/news34.jpeg',
        title: 'საშობაო საჭადრაკო  ტურნირის გამარჯვებული',
        date: '30 დეკემბერი, 2023',
        description: 'მოაწავლეებმა დამრიგებელ ნანა კიკვიძის ხელმძღვანელობით წარმოადგინეს პროექტი "მზის სისტემა"....',
        link: 'News_Feed/news_34.html',
    },
    {
        imageSrc: '/images/gallery/ზეიმი/IIIგ კლასი/event3_1.jpeg',
        title: 'პროექტი "მზის სისტემა"',
        date: '30 დეკემბერი, 2023',
        description: 'მოაწავლეებმა დამრიგებელ ნანა კიკვიძის ხელმძღვანელობით წარმოადგინეს პროექტი "მზის სისტემა"....',
        link: '/Gallery/events/event_3.html',
    },
    {
        imageSrc: '/images/news/news_33/news33.jpeg',
        title: 'საკვირაო სკოლის I მოდულის ოლიმპიადა',
        date: '25 დეკემბერი, 2023',
        description: 'სკოლის I მოდულის ოლიმპიადა IV-VI კლასის მოსწავლეებისთვის...',
        link: '/News_Feed/news_33.html',
    },
    {
        imageSrc: '/images/news/news_32/news32.jpeg',
        title: 'II სადირექციო წერის ნიმუშები (მათემატიკა)',
        date: '25 დეკემბერი, 2023',
        description: 'ანდრია რაზმაძის სახელობის N41 ფიზიკა-მათემატიკის საჯარო სკოლის N2 სადირექციო წერის ნიმუშები',
        link: '/News_Feed/news_32.html',
    },
    {
        imageSrc: 'images/news/news_31/news31.jpg',
        title: '"ტვინების ბრძოლის" რეგიონული ტური',
        date: '19 დეკემბერი, 2023',
        description: '"ბომბი გუნდი" "ტვინების ბრძოლის" რეგიონული ტურის ნახევარფინალში ...',
        link: '/News_Feed/news_31.html',
    },
    {
        imageSrc: '/images/news/news_30/news30.jpeg',
        title: 'II სადირექციო წერის განრიგი',
        date: '18 დეკემბერი, 2023',
        description: 'თუ მოსწავლე ვერ ახერხებს წერაზე გამოცხადებას, მშობელმა ან კანონიერმა...',
        link: '/News_Feed/news_30.html',
    },
    {
        imageSrc: '/images/news/news_29/news29.jpeg',
        title: '"დავით ჩირაძის მემორიალი"',
        date: '18 დეკემბერი, 2023',
        description: 'ქუთაისში გაიმართა "დავით ჩირაძის მემორიალი" 7 წლამდე მოჭადრაკეთა შორის გუნდური ჩემპიონატი...',
        link: '/News_Feed/news_29.html',
    },
    {
        imageSrc: '/images/news/news_28/news28.jpg',
        title: '  შიდასასკოლო შეჯიბრი STEM - ში',
        date: '1 დეკემბერი, 2023',
        description: 'სკოლაში ჩატარდა შიდასასკოლო ჩემპიონატი STEM ოლიმპიადაში ...',
        link: '/News_Feed/news_28.html',
    },
    {
        imageSrc: '/images/news/news_27/news27.png',
        title: ' Lopus - ის ელექტროინჟინერიის წრეზე სიახლეა',
        date: '30 ნოემბერი, 2023',
        description: ' სკოლაში LOPUS-ის ორგანიზებით ჩატარდება STEM ოლიმპიადის ...',
        link: '/News_Feed/news_27.html',
    },
    {
        imageSrc: '/images/news/news_26/news26.jpg',
        title: ' Lopus - ის ელექტროინჟინერიის წრეზე სიახლეა',
        date: '29 ნოემბერი, 2023',
        description: ' წრის მოსწავლეებს დაურიგდათ არდუინოს ნაკრებები რომლებსაც გამოიყენებენ ბევრი საინტერესო პროექტის ასაწყობად ...',
        link: '/News_Feed/news_26.html',
    },
    {
        imageSrc: '/images/news/news_25/news25.jpg',
        title: 'პროგრამა eTwinning-ის 10 წლის იუბილე',
        date: '29 ნოემბერი, 2023',
        description: ' 27 ნოემბერს მასწავლებელთა პროფესიული განვითარების ეროვნული ცენტრის ინიციატივით ...',
        link: '/News_Feed/news_25.html',
    },
    {
        imageSrc: '/images/news/news_24/news24.jpg',
        title: 'პროგრამა eTwinning',
        date: '29 ნოემბერი, 2023',
        description: 'პროგრამა eTwinning-ის ფარგლებში გამართულ კონფერენციაზე ...',
        link: '/News_Feed/news_24.html',
    },
    {
        imageSrc: '/images/jautikovi.jpg',
        title: 'ჟაუტიკოვის მე-20 ოლიმპიადის ამოცანები და ამოხსნები',
        date: '22 ნოემბერი, 2023',
        description: 'ჟაუტიკოვის სახელობის მე-20 ოლიმპიადის შესარჩევი და II ტურის ამოცანები ფიზიკასა და მათემატიკაში...',
        link: '/Projects_and_memoranda/olimpiada/jautikovi/jautikovi.html',
    },
    {
        imageSrc: '/images/additional_news/school_projects/school_project4/school_project4.jpg',
        title: '  „ფიფქია და შვიდი ჯუჯა“',
        date: '22 ნოემბერი, 2023',
        description: 'მე-4გ კლასის მოსწავლეებმა ინგლისურის მასწავლებელ ნათია ყანჩაველის ხელმძღვანელობით წარმოადგინეს პროექტი „ფიფქია და შვიდი ჯუჯა“...',
        link: '/Projects_and_memoranda/school_projects/school_project_4.html',
    },
    {
        imageSrc: '/images/news/news_23/news23.jpg',
        title: '  "ქალები კიბერუსაფრთხოებაში"',
        date: '15 ნოემბერი, 2023',
        description: '„ქალები კიბერუსაფრთხოებაში“ ინიციატივით, TAG International, UKGCP, British Embassy Tbilisi- ს ეგიდით  ...',
        link: '/News_Feed/news_23.html',
    },
    {
        imageSrc: '/images/news/news_22/news22.jpg',
        title: 'ლილე სვანაძე "მაია ჩიბურდანიძის თასის" გამარჯვებულია',
        date: '12 ნოემბერი, 2023',
        description: '  კიდევ ერთი გამარჯვება! მეორეკლასელმა ლილე სვანაძემ ,,მაია ჩიბურდანიძის თასი -2023,, ღია ტურნირზე ...',
        link: '/News_Feed/news_22.html',
    },
    {
        imageSrc: '/images/additional_news/sadireqcio werebi/sadireqcio_werebi.jpg',
        title: '11 კლასი - სადირექციო წერები',
        date: '7 ნოემბერი, 2023',
        description: 'ანდრია რაზმაძის სახელობის N41 ფიზიკა-მათემატიკის საჯარო სკოლის N1 სადირექციო წერები ფიზიკასა და მათემატიკაში',
        link: '/School exams/sadireqcio_werebi/sadireqcio_wera_11.html',
    },
    {
        imageSrc: '/images/additional_news/sadireqcio werebi/sadireqcio_werebi.jpg',
        title: '10 კლასი - სადირექციო წერები',
        date: '7 ნოემბერი, 2023',
        description: 'ანდრია რაზმაძის სახელობის N41 ფიზიკა-მათემატიკის საჯარო სკოლის N1 სადირექციო წერები ფიზიკასა და მათემატიკაში',
        link: '/School exams/sadireqcio_werebi/sadireqcio_wera_10.html',
    },
    {
        imageSrc: '/images/news/news_21/news21.jpg',
        title: '"ტვინების ბრძოლა"',
        date: '7 ნოემბერი, 2023',
        description: ' 27 ოქტომბერს ანდრია რაზმაძის სახელობის N41 ფიზიკა-მათემატიკის საჯარო სკოლაში ჩატარდა გუნდურ-ინტელეტუალური ჩემპიონატი - "ტვინების ბრძოლა"',
        link: '/News_Feed/news_21.html',
    },
    {
        imageSrc: '/images/additional_news/sadireqcio werebi/sadireqcio_werebi.jpg',
        title: '9 კლასი - სადირექციო წერები',
        date: '7 ნოემბერი, 2023',
        description: 'ანდრია რაზმაძის სახელობის N41 ფიზიკა-მათემატიკის საჯარო სკოლის N1 სადირექციო წერები ფიზიკასა და მათემატიკაში',
        link: '/School exams/sadireqcio_werebi/sadireqcio_wera_9.html',
    },
    {
        imageSrc: '/images/additional_news/sadireqcio werebi/sadireqcio_werebi.jpg',
        title: '8 კლასი - სადირექციო წერები',
        date: '7 ნოემბერი, 2023',
        description: 'ანდრია რაზმაძის სახელობის N41 ფიზიკა-მათემატიკის საჯარო სკოლის N1 სადირექციო წერები ფიზიკასა და მათემატიკაში',
        link: '/School exams/sadireqcio_werebi/sadireqcio_wera_8.html',
    },
    {
        imageSrc: '/images/additional_news/sadireqcio werebi/sadireqcio_werebi.jpg',
        title: '7 კლასი - სადირექციო წერები',
        date: '6 ნოემბერი, 2023',
        description: 'ანდრია რაზმაძის სახელობის N41 ფიზიკა-მათემატიკის საჯარო სკოლის N1 სადირექციო წერები ფიზიკასა და მათემატიკაში',
        link: '/School exams/sadireqcio_werebi/sadireqcio_wera_7.html',
    },
    {
        imageSrc: '/images/news/news_20/news20.jpg',
        title: 'სადირექციო წერის განრიგი',
        date: '2 ნოემბერი, 2023',
        description: 'თუ მოსწავლე ვერ ახერხებს წერაზე გამოცხადებას, მშობელმა ან კანონიერმა წარმომადგენელმა ამის შესახებ უნდა შეატყობინოს სკოლას წერამდე...',
        link: '/News_Feed/news_20.html',
    },
    {
        imageSrc: '/images/news/news_19/news19.png',
        title: '„გალფის“ ერთწლიანი სტიპენდია',
        date: '25 ოქტომბერი, 2023',
        description: '100 საუკეთესო პირველკურსელს შორის მოხვედრილი ჩვენი სკოლის 4 კურსდამთავრებული ყოველთვიურად 300 ლარიან სტიპენდიას მიიღებს',
        link: '/News_Feed/news_19.html',
    },
    {
        imageSrc: '/images/additional_news/Lopus Clubs/ელექტროინჟინერია (Arduino) I ჯგუფი (copy).png',
        title: 'Lopus Electronics ის საგანმანათლებლო წრეები',
        date: '17 ოქტომბერი, 2023',
        description: 'ანდრია რაზმაძის სახელობის N41 საჯარო სკოლაში 17 ოქტომბერს ფუნქციონირებას იწყებს Lopus Electronics-ის წრეები',
        link: '/Clubs and Curses/clubs/lopus.html',
    },
    {
        imageSrc: '/images/news/news_18/news18.jpg',
        title: 'სკოლის ავტორიზაცია',
        date: '16 ოქტომბერი, 2023',
        description: '2023 წლის 13 ოქტომბერს, ანდრია რაზმაძის სახელობის N41 ფიზიკა-მათემატიკის საჯარო სკოლამ წარმატებით გაიარა ავტორიზაცია და ეს სტატუსი მიენიჭა 6 წლის ვადით!',
        link: '/News_Feed/news_18.html',
    },
    {
        imageSrc: '/images/news/news_17/news17.jpg',
        title: 'ტრენინგ-კურსი „ენერგოეფექტურობა და მწვანე შენობები“',
        date: '4 ოქტომბერი, 2023',
        description: 'ქუთაისის მუნიციპალიტეტში წარმატებით მიმდინარეობს ევროკავშირის (EU) და გაეროს განვითარების პროგრამის (UNDP) ინიციატივა “მერები ეკონომიკური ზრდისთვის”',
        link: '/News_Feed/news_17.html',
    },
    {
        imageSrc: '/images/news/news_16/news16.jpg',
        title: 'GREDA-სა და USAID-ის ენერგეტიკული მომავლის უზრუნველყოფის პროგრამა',
        date: '4 ოქტომბერი, 2023',
        description: 'GREDA-სა და USAID-ის ენერგეტიკული მომავლის უზრუნველყოფის პროგრამის ერთობლივი საგანმანათლებლო პროექტის შემაჯამებელი ღონისძიება',
        link: '/News_Feed/news_16.html',
    },
    {
        imageSrc: '/images/news/news_15/news15.jpg',
        title: 'არდუინოს პროგრამირებისა და ელექტროინჟინერიის წრე',
        date: '3 ოქტომბერი, 2023',
        description: 'ანდრია რაზმაძის სახელობის N41 საჯარო სკოლაში ფუნქციონირებას იწყებს არდუინოს პროგრამირებისა და ელექტროინჟინერიის წრე',
        link: '/News_Feed/news_15.html',
    },
    {
        imageSrc: '/images/news/news_14/news14.jpg',
        title: ' საიტების აწყობის წრე',
        date: '3 ოქტომბერი, 2023',
        description: 'ანდრია რაზმაძის სახელობის N41 საჯარო სკოლაში ფუნქციონირებას იწყებს საიტების აწყობის წრე',
        link: '/News_Feed/news_14.html',
    },
    // {
    //     imageSrc: '/images/news/news_13/news13.jpg',
    //     title: ' ანდროიდ აპლიკაციების აწყობის კურსი',
    //     date: '3 ოქტომბერი, 2023',
    //     description: 'ანდრია რაზმაძის სახელობის N41 საჯარო სკოლაში ფუნქციონირებას იწყებს ანდროიდ აპლიკაციების აწყობის კურსი',
    //     link: '/News_Feed/news_13.html',
    // },
    {
        imageSrc: '/images/news/news_12/news12.jpg',
        title: ' WRO - ლეგოს რობოტიკის წრე',
        date: '3 ოქტომბერი, 2023',
        description: 'ანდრია რაზმაძის სახელობის N41 საჯარო სკოლის და  Lopus Electronics ის თანამშრომლობის ფარგლებში ფუნქციონირებას იწყებს  ლეგოს რობოტიკის წრე',
        link: '/News_Feed/news_12.html',
    },
    {
        imageSrc: '/images/news/news_11/news11.jpg',
        title: 'სკოლის წარჩინებულ 9 მოსწავლეს პორტატული კომპიუტერები გადასცეს',
        date: '28 სექტემბერი, 2023',
        description: 'ანდრია რაზმაძის სახელობის ქუთაისის N41 ფიზიკა-მათემატიკის საჯარო სკოლის წარჩინებულ 9 მოსწავლეს პორტატული კომპიუტერები გადასცეს',
        link: '/News_Feed/news_11.html',
    },
    {
        imageSrc: '/images/news/news_10/news10.jpg',
        title: 'პოლონეთის ქალაქ პოზნანის დელეგაციის ვიზიტი სკოლაში',
        date: '25 სექტემბერი, 2023',
        description: 'დელეგაცია ვიზიტის ფარგლებში ესტუმრა სკოლას, სტუმართა შორის იმყოფებოდნენ რესურსცენტრის ხელმძღვანელი პირები და ქალაქის 7 სკოლის დირექტორები მოადგილეებთან ერთად.',
        link: '/News_Feed/news_10.html',
    },
    {
        imageSrc: '/images/additional_news/finansuri_forma/finansuri_forma.jpg',
        title: '  2022 წლის ფინანსური ანგარიშგების ფორმა',
        date: '20 სექტემბერი, 2023',
        description: 'სსიპ ანდრია რაზმაძის სახელობის N41 ფიზიკა-მათემატიკის საჯარო სკოლის 2022 წლის ფინანსური ანგარიშგების ფორმა',
        link: '/About_Us/saswavlo_gegma/finansuri_forma.html',
    },
    {
        imageSrc: '/images/news/news_9/news9.jpg',
        title: '  "ნიჭიერთა საღამო სკოლის" წრე ფიზიკასა და მათემატიკაში',
        date: '18 სექტემბერი, 2023',
        description: '"ნიჭიერთა სკოლა" (იგივე "საღამოს სკოლა") აცხადებს მოსწავლეთა მიღებას 2023-2024 სასწავლო წლისათვის',
        link: '/News_Feed/news_9.html',
    },
    {
        imageSrc: '/images/news/news_8/news8.jpg',
        title: 'ეროვნული სასწავლო გეგმა 2023-2024',
        date: '15 სექტემბერი, 2023',
        description: 'სსიპ ანდრია რაზმაძის სახელობის N41 ფიზიკა-მათემატიკის საჯარო სკოლის სასკოლო სასწავლო გეგმა',
        link: '/News_Feed/news_8.html',
    },
    {
        imageSrc: '/images/news/news_7/news7.jpg',
        title: 'შინაგანაწესი 2023-2024',
        date: '15 სექტემბერი, 2023',
        description: 'სსიპ ანდრია რაზმაძის სახელობის ქ.ქუთაისის N41 ფიზიკა-მათემატიკის საჯარო სკოლის შინაგანაწესი',
        link: '/News_Feed/news_7.html',
    },
    {
        imageSrc: '/images/news/news_6/news6.jpg',
        title: 'პროექტი „წითელი ნაკვალევი“',
        date: '9 სექტემბერი, 2023',
        description: '"სკოლის მასწავლებელთა ონლაინ სისტემაში ჩართვა და დამეგობრება ევროპის ქვეყნების მასწავლებლებთან" (eTwinning Plus) ელჩი/ტრენერი ნინო ჩხეტია ჩაატარა პროექტი „წითელი ნაკვალევი“',
        link: '/News_Feed/news_6.html',
    },
    {
        imageSrc: '/images/news/news_5/news5.jpg',
        title: '25 ოქტომბერი სკოლებში მედიაწიგნიერების დღეა',
        date: '9 სექტემბერი, 2023',
        description: '25 ოქტომბერი სკოლებში მედიაწიგნიერების დღეა. სწორედ ამ თემაზე ქართული ენისა და ლიტერატურის მასწავლებლის, ნინო ჩხეტიას ორგანიზებით ჩატარდა გაკვეთილი',
        link: '/News_Feed/news_5.html',
    },
    {
        imageSrc: '/images/news/news_4/news4.jpg',
        title: '„წიგნების თაროს“ XIII სეზონის წარმატებული გუნდი',
        date: '9 სექტემბერი, 2023',
        description: '„წიგნების თაროს“ XIII სეზონის გამარჯვებული ანდრია რაზმაძის ქალაქ ქუთაისის N41 ფიზიკა-მათემატიკის საჯარო სკოლის გუნდი გახდა.',
        link: '/News_Feed/news_4.html',
    },
    {
        imageSrc: '/images/news/news_3/news3.png',
        title: 'საკვირაო სკოლის განცხადება 2023-2024',
        date: '6 სექტემბერი, 2023',
        description: 'ქუთაისის ანდრია რაზმაძის სახელობის ფიზიკა - მათემატიკური 41-ე საჯარო სკოლასთან არსებული საკვირაო სკოლა აცხადებს მოსწავლეების მიღებას 2023-2024 სასწავლო წლისთვის.',
        link: '/News_Feed/news_3.html',
    },
    {
        imageSrc: '/images/news/news_2/news2.jpg',
        title: 'მსოფლიოს 35-ე ოლიმპიადა ინფორმატიკაში',
        date: '4 სექტემბერი, 2023',
        description: 'მსოფლიოს 35-ე ოლიმპიადა ინფორმატიკაში უნგრეთის ქალაქ სეგედში 28 აგვისტოს დაიწყო და 4 სექტემბერს დასრულდა, მასში 90 ქვეყნის 355 უძლიერესი მოსწავლე მონაწილეობდა.',
        link: '/News_Feed/news_2.html',
    },
    {
        imageSrc: '/images/news/news_1/news1.jpg',
        title: 'გამარჯვებული პროექტი — SAFE SPACE',
        date: '31 აგვისტო, 2023',
        description: 'ქუთაისის, თბილისის, ხაშურისა და სენაკის სკოლების მოსწავლეები — ათასწლეულის ინოვაციის კონკურსის გამარჯვებული გუნდის, Atemporal-ის წევრები, მათი პირველი მოგზაურობიდან დაბრუნდნენ.',
        link: '/News_Feed/news_1.html',
    }
];
