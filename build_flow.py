from pathlib import Path
from html import escape
import re

ROOT = Path(__file__).parent
MAIL = 'mailto:ptstjaipur@yahoo.com'
PTST = 'https://www.ptst.in/'

# Each workbook branch has its own landing page. Verified PTST resources remain
# on PTST's existing services; enquiry links are used when no public URL exists.
PAGES = {
 'about': {
  'title':'Our story', 'label':'The trust', 'intro':'A living centre for Jain knowledge in Jaipur, shaped by study, service and the pursuit of self-understanding.',
  'sections':[
   ('inspiration','The inspiration','The Trust grew with the spiritual inspiration of Pujya Shri Kanjiswami and a commitment to share Jain tattvagyan.',['Pujya Shri Kanjiswami|His teachings remain an important source of inspiration for the Trust.|https://www.ptst.in/about-us.php','The life and thought of Pandit Todarmal|Explore the scholarly tradition that gives the Trust its name.|https://www.ptst.in/about-us.php']),
   ('founder','Founder and legacy','The Smarak Bhawan was built through the initiative of Shri Puranchand Godika. The Trust was established in 1967 in Jaipur.',['Shri Puranchand Godika|Read the Trust’s account of its founding and continuing work.|https://www.ptst.in/about-us.php','Our activities and achievements|See the work of the Trust across learning and community life.|https://www.ptst.in/about-us.php']),
   ('gallery','Photo gallery','Explore the campus and its activities through the Trust’s published galleries.',['Mahavidyalaya gallery|Photographs from the institution and its community.|https://www.ptst.in/sidhant-mahavidyalaya-gallery.php','Smarak Bhawan|Learn about the spaces that bring the community together.|spaces.html'])]},
 'learning': {
  'title':'Learn with PTST', 'label':'Our activities', 'intro':'From formal scholarship to study at home, find a path into Jain philosophy and values.',
  'sections':[
   ('sahitya','Sahitya and scholarship','Literature and careful study sit at the heart of the Trust’s educational work.',['Books and publications|Explore PTST’s book and PDF resources.|library.html#books','Shastri corner|Resources for students and graduates.|https://www.ptst.in/shastri-corner.php']),
   ('mahavidyalaya','Siddhant Mahavidyalaya','Shri Todarmal Digamber Jain Siddhant Mahavidyalaya is a centre for sustained study of Jain thought.',['Introduction|Learn about the Mahavidyalaya.|https://www.ptst.in/sidhant-mahavidyalaya-introduction.php','Faculty and routine|View teachers and the daily schedule through PTST.|https://www.ptst.in/sidhant-mahavidyalaya-teachers.php','Syllabus|See the published course structure.|https://www.ptst.in/sidhant-mahavidyalaya-syllabus.php','Admissions|Read the current rules and application information.|https://www.ptst.in/sidhant-mahavidyalaya-admission-form.php']),
   ('pareeksha','Veetrag Vigyan Pareeksha Board','A structured route to learning, assessment and deeper engagement with Jain principles.',['Board introduction|Explore its aims and examination work.|https://www.ptst.in/pareeksha-board-introduction.php','Admission forms|Find the board’s published forms and instructions.|https://www.ptst.in/pareeksha-board-admission-forms.php']),
   ('mukt','Todarmal Mukt Vidhya Peeth','Open learning for people who wish to study beyond a conventional classroom.',['Introduction and syllabus|Explore the programme and subjects.|https://www.ptst.in/mukt-vidyapeeth-introduction.php','Apply online|Continue to PTST’s application service.|https://www.ptst.in/ptst-admin/registration_mukt.php']),
   ('arham','Arham Pathshala','A learning space for young minds and families.',['Introduction|Read the Pathshala introduction published by PTST.|https://ptst.in/images/arham_intro.pdf','Registration|Go to the Pathshala registration service.|https://arham.ptst.live/']),
   ('alumni','Snatak Parishad & alumni','The workbook includes an alumni path for graduates to remain connected.',['Graduate list|Open PTST’s Snatak list.|https://www.ptst.in/ptst-admin/snatak_list.php','Snatak registration|Register through PTST’s service.|https://www.ptst.in/ptst-admin/registration_snatak.php'])]},
 'library': {
  'title':'Library & literature', 'label':'Read and research', 'intro':'A gateway to books, manuscripts, study material and the recorded word.',
  'sections':[
   ('start','Begin in the library','Explore the collection by format and subject, then continue into PTST’s live catalogue.',['Library introduction|Start with the Trust’s books and study resources.|https://library.ptst.live/','Browse categories|Search the catalogue by title, author and subject.|https://library.ptst.live/','Collection at a glance|The live catalogue currently lists more than 8,000 books; check it for the latest total.|https://library.ptst.live/','New and available material|Browse PTST’s current downloadable collection.|https://www.ptst.in/pdf/suchipatra_pdf_books.php']),
   ('daily','Daily gatha & reflection','The proposed flow includes a new gatha and quote each day. The homepage offers a daily reflection prompt; a scripture feed awaits verses approved by PTST.',['Today’s reflection|Read a short prompt for self-study.|index.html#daily-reflection','Scripture collection|Browse source texts and books through PTST.|https://www.ptst.in/pdf/suchipatra_pdf_books.php']),
   ('books','Books and publications','Find literature for sustained enquiry, from introductory study to deeper research.',['Library catalogue|Search the Acharya Kund-Kund Saraswati Pustakalaya catalogue.|https://library.ptst.live/','PDF books|Browse the Trust’s downloadable book collection.|https://www.ptst.in/pdf/suchipatra_pdf_books.php','Buy books online|Open PTST’s existing book shop.|https://www.ptst.in/ptst/books/index.php','Book list|View PTST’s published sahitya list.|https://www.ptst.in/pdf/suchipatra_pdf_books.php']),
   ('digital','Digital resources','Continue your reading through the Trust’s online study material.',['Jain Pathpardarshak|Access the Trust’s study resources.|https://www.ptst.in/pdf/jain_pathpardarshak.php','Veetrag Vigyan|Explore educational material and publications.|https://www.ptst.in/pdf/vitrag_vigyan.php','Shrutskand|Ask the Trust about this collection and its significance.|'+MAIL]),
   ('audio','Audio library','Listen to pravachans, readings and devotional recordings.',['Pravachan MP3|Browse the Trust’s audio collection.|https://www.ptst.in/mp3/mp3_all.php','Audio books|Find spoken literature on PTST’s resource site.|https://www.ptst.in/mp3/audio_book.php','Pujan, path and bhajan|Explore devotional audio through PTST.|https://www.ptst.in/']),
   ('shrutskand','Shrutskand Rachna','The workbook reserves space for a photograph and explanation of the Shrutskand Rachna. The Trust can provide the approved image and description.',['Request the official photograph|Contact PTST for the approved visual and context.|'+MAIL,'Explore related literature|Continue to the catalogue while this feature is prepared.|https://library.ptst.live/'])]},
 'programmes': {
  'title':'Spiritual & youth programmes', 'label':'Learn together', 'intro':'Study, practice and shared experiences for seekers of different ages and stages.',
  'sections':[
   ('adhyatmik','Aadhyatmik Shikshan Shivir','Immersive spiritual learning and reflection through the Trust’s shivir tradition.',['Programme enquiry|Ask about format, eligibility and upcoming sessions.|'+MAIL,'August session|See the events and schedule hub for updates.|events.html#calendar','October session|See the events and schedule hub for updates.|events.html#calendar']),
   ('prashikshan','Prashikshan Shivir','Training and guided study for those supporting Jain education in their communities.',['Programme information|Visit the Prashikshan Shivir site.|https://prashikshan.ptst.live/','Enquire|Contact PTST for participation details.|'+MAIL]),
   ('yatra','Yatra and group shivir','Learning journeys and group sessions deepen reflection through community.',['Yatra enquiries|Contact the Trust for current opportunities.|'+MAIL,'Group shivir|Ask about organising or joining a group session.|'+MAIL]),
   ('arham-fest','Arham Fest','A community gathering rooted in learning, values and connection.',['Event enquiries|Ask the Trust about the next gathering.|'+MAIL,'Explore other events|Go to the schedule hub.|events.html'])]},
 'spaces': {
  'title':'Smarak Bhawan', 'label':'Places of reflection', 'intro':'Explore the physical spaces that bring study, worship and community together in Jaipur.',
  'sections':[
   ('panchteerth','Panchteerth Jinalay','A sacred space within the Smarak Bhawan setting.',['Plan a visit|Contact the Trust for visiting information.|contact.html#visit','Photo gallery|Ask for the current campus gallery.|'+MAIL]),
   ('seemandhar','Seemandhar Jinalay','A place for reverence and quiet reflection.',['Visit the campus|Find the Trust’s address and contact details.|contact.html#visit']),
   ('pravachan','Pravachan Hall','A gathering space for discourses and shared learning.',['Listen to discourses|Browse audio and video resources.|media.html','Programme enquiries|Contact the Trust about sessions.|'+MAIL]),
   ('bookstore','Book store','Continue your study with literature from PTST.',['Shop books|Open the Trust’s book service.|https://www.ptst.in/ptst/books/index.php'])]},
 'events': {
  'title':'Events & schedule', 'label':'Gather and grow', 'intro':'Find the programme types in the Trust’s flow. Confirm current dates and registration with PTST before planning a visit.',
  'sections':[
   ('calendar','Programme calendar','The workbook names recurring programme windows; dates are shared by the Trust when announced.',['Aadhyatmik Shikshan Shivir — August|Ask for the next confirmed dates.|'+MAIL,'Aadhyatmik Shikshan Shivir — October|Ask for the next confirmed dates.|'+MAIL,'Prashikshan Shivir|Visit the programme site for current information.|https://prashikshan.ptst.live/']),
   ('festivals','Festivals and gatherings','Celebrate learning and community throughout the year.',['Daslakshan|Enquire about current observances.|'+MAIL,'Annual function|Ask PTST for the current programme.|'+MAIL,'Arham Fest|Discover the programme overview.|programmes.html#arham-fest'])]},
 'journal': {
  'title':'News & writing', 'label':'Ideas to carry forward', 'intro':'Follow the Trust’s publications, educational work and community updates.',
  'sections':[
   ('veetrag','Veetrag Vigyan','Explore the Pareeksha Board and its periodical archive.',['About the board|Read the Trust’s official overview.|https://www.ptst.in/pareeksha-board-introduction.php','Dated magazine issues|Browse PTST’s Veetrag Vigyan archive.|https://www.ptst.in/pdf/vitrag_vigyan.php']),
   ('jainpath','Jainpath','Read Jain Path Pradarshak material from PTST’s archive.',['Browse issues|Open the Trust’s published collection.|https://www.ptst.in/pdf/jain_pathpardarshak.php','Enquire about articles|Ask PTST about submissions and current issues.|'+MAIL]),
   ('updates','Trust updates','For confirmed announcements, contact the Trust or visit its current site.',['Official PTST website|Check updates at the source.|https://www.ptst.in/','Events and schedule|Explore programme categories.|events.html','PTST Facebook|Follow the Trust’s published social updates.|https://www.facebook.com/ptst.jaipur/'])]},
 'media': {
  'title':'Video & audio', 'label':'Listen and reflect', 'intro':'Discourses, introductions and recordings that can accompany your learning wherever you are.',
  'sections':[
   ('discourses','Pravachan and subject videos','Listen to teachings and explore themes in Jain thought.',['PTST YouTube channel|Watch the Trust’s published videos.|https://www.youtube.com/user/todarmalsmaraktrust','PTST playlists|Browse videos by subject on the official channel.|https://www.youtube.com/user/todarmalsmaraktrust/playlists','MP3 pravachan|Listen through the Trust’s audio archive.|https://www.ptst.in/mp3/mp3_all.php']),
   ('collections','Special and occasion videos','Find introductions, festival recordings and curated talks.',['Video channel|Browse the published collection.|https://www.youtube.com/user/todarmalsmaraktrust','Pujya Kanjiswami and Dr. Hukamchand Bharill|Explore recordings linked from PTST.|https://www.ptst.in/']),
   ('audio','Audio library','Readings, pravachans and devotional audio in one place.',['Audio resources|Open the library’s audio path.|library.html#audio','Jinvani live|Visit PTST’s linked live stream.|https://live.jinvanichannel.com/'])]},
 'shop': {
  'title':'Books & shop', 'label':'Bring wisdom home', 'intro':'Find literature and enquire about other items named in the Trust’s proposed shop flow.',
  'sections':[
   ('sahitya','Sahitya','Browse publications through PTST’s existing store.',['Buy books online|Continue to the Trust’s book shop.|https://www.ptst.in/ptst/books/index.php','Explore the catalogue|Search books in the library catalogue.|https://library.ptst.live/']),
   ('frames','Panchteerth photo frames','The workbook includes photo frames in its shop plan. Availability and ordering are confirmed by PTST.',['Ask about availability|Email the Trust for current options.|'+MAIL])]},
 'support': {
  'title':'Support & stay', 'label':'Be part of the work', 'intro':'Help sustain learning and connect with the Trust about a visit or stay.',
  'sections':[
   ('donate','Donate','Support PTST’s educational and community work using its official donation service.',['Donate through PTST|Open the Trust’s official donation page.|https://www.ptst.in/paydonation.php','Donation details|Review information on the Trust’s website.|https://www.ptst.in/paydonation.php']),
   ('stay','Stay and visit','The proposed site flow includes accommodation. Ask PTST about current availability, eligibility and arrangements.',['Stay enquiry|Email the Trust before making travel plans.|'+MAIL,'Visit information|Find the address and contact details.|contact.html#visit']),
   ('volunteer','Get involved','Connect with the team to learn how you can contribute to study, programmes or service.',['Contact the Trust|Start a conversation about ways to help.|'+MAIL])]},
 'contact': {
  'title':'Contact & visit', 'label':'We would love to hear from you', 'intro':'Questions about a programme, publication or visit? Connect directly with Pandit Todarmal Smarak Trust.',
  'sections':[
   ('visit','Visit the Trust','A-4, Bapu Nagar, Jaipur, Rajasthan 302015.',['Map and directions|Open the location in Google Maps.|https://www.google.com/maps/search/?api=1&query=Pandit+Todarmal+Smarak+Trust+Jaipur','Call PTST|+91 89490 33694|tel:+918949033694']),
   ('write','Write to us','For admissions, events, accommodation or publications, the Trust can guide you to the right team.',['Email PTST|ptstjaipur@yahoo.com|'+MAIL,'Official contact page|Find current contact information on PTST’s website.|https://www.ptst.in/contact.php'])]}
}

NAV = [ ('Home','index.html'),('E-Library','library.html'),('Our Activities','learning.html'),('Spiritual & Youth','programmes.html'),('Events & Schedule','events.html'),('News & Blog','journal.html'),('Video & Audio','media.html'),('Shop','shop.html'),('Contact Us','contact.html'),('About Us','about.html') ]
FLOW = [ ('About & inspiration','about.html','Founder, legacy and gallery'),('Our activities','learning.html','Sahitya and four learning institutions'),('E-library','library.html','Books, digital and audio'),('Spiritual & youth','programmes.html','Shivirs, yatra and Arham Fest'),('Smarak Bhawan','spaces.html','Jinalays, hall and book store'),('Events & schedule','events.html','Programme windows and festivals'),('News & blog','journal.html','Veetrag Vigyan, Jainpath and updates'),('Video & audio','media.html','Discourses, talks and recordings'),('Shop','shop.html','Sahitya and photo frames'),('Stay & donate','support.html','Visits, stay and giving'),('Contact','contact.html','Address, phone and email') ]
HOME_LINKS = [
 ('Introduction','about.html'),('Inspiration','about.html#inspiration'),('Founder','about.html#founder'),('Sahitya','learning.html#sahitya'),
 ('E-library','library.html'),('Stay','support.html#stay'),('Donation','support.html#donate'),('Photo gallery','about.html#gallery'),
 ('Events','events.html'),('Siddhant Mahavidyalaya','learning.html#mahavidyalaya'),('Veetrag Vigyan Pareeksha Board','learning.html#pareeksha'),
 ('Mukt Vidhya Peeth','learning.html#mukt'),('Arham Pathshala','learning.html#arham'),('Aadhyatmik Shikshan Shivir','programmes.html#adhyatmik'),
 ('Prashikshan Shivir','programmes.html#prashikshan'),('Veetrag Vigyan','journal.html#veetrag'),('Jainpath','journal.html#jainpath'),
 ('Video','media.html#discourses'),('Audio','library.html#audio'),('Articles','journal.html'),('Social media','journal.html#updates')]

def link(href, label, cls=''):
    ext = href.startswith('https://')
    return f'<a class="{cls}" href="{escape(href, quote=True)}"' + (' target="_blank" rel="noopener noreferrer"' if ext else '') + f'>{escape(label)} <span aria-hidden="true">↗</span></a>'

def header():
    nav = ''.join(f'<a href="{href}">{name}</a>' for name,href in NAV)
    return f'''<a class="skip-link" href="#main">Skip to content</a><div class="utility-bar"><div class="container utility-inner"><span>✧ &nbsp;Rooted in Jaipur since 1967</span><div><a href="contact.html#visit">Visit us</a><span class="utility-separator"></span><a href="contact.html">Contact</a></div></div></div><header class="site-header" id="top"><div class="container header-inner"><a class="brand" href="index.html" aria-label="Pandit Todarmal Smarak Trust, home"><img src="logo.webp" alt="Pandit Todarmal Smarak Trust" width="699" height="69"></a><div class="header-actions"><div class="social-links" aria-label="PTST social media"><a href="https://www.facebook.com/ptst.jaipur/" target="_blank" rel="noopener noreferrer" aria-label="PTST on Facebook">f</a><a href="https://www.youtube.com/user/todarmalsmaraktrust" target="_blank" rel="noopener noreferrer" aria-label="PTST on YouTube">▶</a></div><a class="text-action stay-action" href="support.html#stay">Stay</a><a class="button button-dark header-cta" href="support.html#donate">Donate <span aria-hidden="true">↗</span></a><button class="menu-toggle" type="button" aria-label="Open menu" aria-expanded="false" aria-controls="mobile-menu"><span></span><span></span><span></span></button></div></div><nav class="desktop-nav site-nav" aria-label="Main navigation"><div class="container">{nav}</div></nav><nav class="mobile-nav" id="mobile-menu" aria-label="Mobile navigation" hidden>{nav}<a href="spaces.html">Smarak Bhawan</a><a href="support.html#stay">Stay</a><a href="support.html#donate">Donate</a></nav></header>'''

def footer():
    return '''<footer id="contact"><div class="container footer-main"><div class="footer-brand"><img src="logo.webp" alt="Pandit Todarmal Smarak Trust" width="699" height="69"><p>Learning. Reflection. Service.</p></div><div class="footer-links"><div><strong>Explore</strong><a href="flow.html">Full site flow</a><a href="learning.html">Institutions</a><a href="library.html">Library</a><a href="events.html">Events</a></div><div><strong>Connect</strong><a href="programmes.html">Programmes</a><a href="support.html">Support & stay</a><a href="contact.html">Visit us</a><a href="mailto:ptstjaipur@yahoo.com">Email PTST</a></div></div></div><div class="container footer-bottom"><span>© <span id="year">2026</span> Pandit Todarmal Smarak Trust</span><span>Made with reverence for knowledge.</span><a href="#top">Back to top ↑</a></div></footer>'''

def card(raw):
    title, desc, href = raw.split('|',2)
    return f'<article class="resource-card"><h3>{escape(title)}</h3><p>{escape(desc)}</p>{link(href,"Explore")}</article>'

def section(item, i):
    ident, title, intro, cards = item
    return f'''<section class="detail-section" id="{ident}"><div class="container detail-layout"><div class="detail-lead"><p class="eyebrow">{i:02d} / Explore</p><h2>{escape(title)}</h2><p>{escape(intro)}</p></div><div class="resource-grid">{''.join(card(x) for x in cards)}</div></div></section>'''

def page(slug, data):
    toc = ''.join(f'<a href="#{ident}">{escape(title)} <span>↗</span></a>' for ident,title,_,_ in data['sections'])
    body = ''.join(section(x,i) for i,x in enumerate(data['sections'],1))
    html = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#f8f4ec"><meta name="description" content="{escape(data['intro'],quote=True)}"><title>{escape(data['title'])} | Pandit Todarmal Smarak Trust</title><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@400;500;600&display=swap" rel="stylesheet"><link rel="stylesheet" href="styles.css"><link rel="stylesheet" href="flow.css"><script src="script.js" defer></script></head><body>{header()}<main id="main"><section class="page-hero"><div class="container"><p class="eyebrow light">{escape(data['label'])}</p><h1>{escape(data['title'])}<em>.</em></h1><p>{escape(data['intro'])}</p><a href="flow.html" class="page-back">← View the full site flow</a></div></section><nav class="page-toc" aria-label="On this page"><div class="container">{toc}</div></nav>{body}<section class="detail-cta"><div class="container"><div><p class="eyebrow light">Continue the conversation</p><h2>Every question is a beginning.</h2></div>{link('contact.html','Connect with PTST','button button-cream')}</div></section></main>{footer()}</body></html>'''
    (ROOT / f'{slug}.html').write_text(html,encoding='utf-8')

for slug,data in PAGES.items(): page(slug,data)

flow_cards = ''.join(f'<a class="flow-card" href="{href}"><span>{i:02d}</span><h2>{escape(title)}</h2><p>{escape(desc)}</p><b aria-hidden="true">↗</b></a>' for i,(title,href,desc) in enumerate(FLOW,1))
flow = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="Explore the complete Pandit Todarmal Smarak Trust website flow."><title>Explore PTST | Full site flow</title><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@400;500;600&display=swap" rel="stylesheet"><link rel="stylesheet" href="styles.css"><link rel="stylesheet" href="flow.css"><script src="script.js" defer></script></head><body>{header()}<main id="main"><section class="page-hero"><div class="container"><p class="eyebrow light">A place for every path</p><h1>Explore PTST<em>.</em></h1><p>Follow the complete journey through learning, literature, spiritual activities, the Smarak Bhawan, events and ways to connect.</p></div></section><section class="flow-section"><div class="container"><p class="eyebrow">Your guide</p><div class="flow-grid">{flow_cards}</div></div></section></main>{footer()}</body></html>'''
(ROOT/'flow.html').write_text(flow,encoding='utf-8')

index = (ROOT/'index.html').read_text(encoding='utf-8-sig')
index = re.sub(r'<a class="skip-link".*?</header>', header(), index, count=1, flags=re.S)
index = re.sub(r'<footer id="contact">.*?</footer>', footer(), index, count=1, flags=re.S)
if '<link rel="stylesheet" href="flow.css">' not in index:
    index = index.replace('<link rel="stylesheet" href="styles.css">','<link rel="stylesheet" href="styles.css"><link rel="stylesheet" href="flow.css">')
index = index.replace('href="#pathways">Explore PTST','href="flow.html">Explore PTST')
index = index.replace('href="#pathways">Begin exploring','href="flow.html">Begin exploring')
index = index.replace('href="#about">Discover our story','href="about.html">Discover our story')
index = index.replace('href="#institutions"','href="learning.html"').replace('href="#library"','href="library.html"').replace('href="#media"','href="media.html"').replace('href="#events"','href="events.html"')
index = index.replace('href="#contact"','href="contact.html"')
index = index.replace('href="#about"','href="about.html"')
index = index.replace('href="https://library.ptst.live/"','href="library.html"')
index = index.replace('href="mailto:ptstjaipur@yahoo.com?subject=Enquiry%20about%20PTST"','href="contact.html"')
index = index.replace('href="mailto:ptstjaipur@yahoo.com"','href="contact.html"')
index = index.replace('href="#visit"','href="contact.html#visit"')
index = index.replace('<span>01 / 03</span><span class="caption-rule"></span><span>Jaipur, Rajasthan</span>', '<span>Jaipur, Rajasthan</span><span class="caption-rule"></span><span>Since 1967</span>')
index = index.replace('href="contact.html" aria-label="Ask about audio and video resources"', 'href="media.html" aria-label="Explore audio and video resources"')
for description, target in [
    ('A dedicated centre for the study of Jain philosophy and tradition.', 'learning.html#mahavidyalaya'),
    ('Structured learning that encourages thoughtful engagement with Jain principles.', 'learning.html#pareeksha'),
    ('Creating opportunities to learn beyond the boundaries of a classroom.', 'learning.html#mukt'),
    ('Introducing children to values, curiosity and compassionate living.', 'learning.html#arham')]:
    index = index.replace(f'{description}</p></article>', f'{description}</p><a class="institution-link" href="{target}">Explore institution ↗</a></article>')
index = re.sub(r'<section class="home-reflection">.*?</section>', '', index, flags=re.S)
index = re.sub(r'<section class="home-updates">.*?</section>', '', index, flags=re.S)
index = index.replace('<section class="intro-strip"', '<section class="home-updates"><div class="container updates-layout"><div class="updates-lead"><span class="eyebrow">New & noteworthy</span><strong>Continue the journey</strong></div><a href="https://www.youtube.com/user/todarmalsmaraktrust" target="_blank" rel="noopener noreferrer"><span class="update-icon">▶</span><span><b>Intro video & discourses</b><small>Watch on the official PTST channel</small></span><i>↗</i></a><a href="https://www.ptst.in/" target="_blank" rel="noopener noreferrer"><span class="update-icon">✧</span><span><b>Latest Trust updates</b><small>Check PTST’s current notices</small></span><i>↗</i></a><a href="events.html"><span class="update-icon">◷</span><span><b>Events & schedule</b><small>Programmes and observances</small></span><i>↗</i></a></div></section><section class="intro-strip"')
index = index.replace('<section class="home-flow"', '<section class="home-reflection"><div class="container reflection-inner"><div><p class="eyebrow">A moment each day</p><h2>Pause. Reflect. <em>Begin again.</em></h2><p id="daily-reflection">What can I understand more clearly today?</p><span class="reflection-note">A daily reflection prompt, inspired by the spirit of self-study.</span></div><div class="reflection-links"><a href="library.html">Explore the literature <span>↗</span></a><a href="media.html">Watch and listen <span>↗</span></a></div></div></section><section class="home-flow"')
index = re.sub(r'<section class="home-flow">.*?</section>', '', index, flags=re.S)
index = index.replace('<section class="visit-section"', '<section class="home-flow"><div class="container"><div class="section-heading"><div><p class="eyebrow">The complete journey</p><h2>Explore every <em>path.</em></h2></div><p>The homepage paths in your website flow, gathered in one place.</p></div><div class="home-flow-grid">' + ''.join(f'<a href="{href}">{escape(title)} <span>↗</span></a>' for title,href in HOME_LINKS) + '</div><a class="flow-all" href="flow.html">View the complete site guide ↗</a></div></section><section class="visit-section"')
(ROOT/'index.html').write_text(index,encoding='utf-8')
print('Built',len(PAGES)+2,'pages')
