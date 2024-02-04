from Account import Account
from Pitch import Pitch
from Database import PitchDatabase, AccountDatabase
import numpy as np
from Manage import ManageGeneral

def model():
    user = Account("mwalsh", "1234", "Mikayla Walsh", "mikayla_walsh@brown.edu", "I have worked in projects beofore specializing in back end development. I also have experience working with machine learning models.", "I am a Junior at Brown studying Computer Science. I am looking for a partner who is determined and passionate.")
    pitch00 = user.create_pitch("Space Out", "I had an idea for a place when entrepreneuers can come together with their craziest ideas that they come up with when they zone out and let their imagination run free.", "Website", user.about_me)
    pitch000 = user.create_pitch("GreenThumb App", "Imagine an app that helps people discover and care for various plant species. From gardening tips to plant identification, this app will make plant enthusiasts' lives easier.", "Mobile App Development", user.about_me)

    manager = ManageGeneral(user)

    user1 = Account("john_doe", "password123", "John Doe", "john.doe@example.com", "Experienced software developer with expertise in web development and cloud services. Passionate about creating innovative solutions.", "A creative and motivated partner for new project.")
    pitch1 = user1.create_pitch("EcoHub", "I envision a platform where eco-conscious individuals can connect, share ideas, and collaborate on projects that promote sustainability.", "Website", user1.about_me)
    pitch5 = user1.create_pitch("FoodExplorer", "A mobile app that helps users discover new and exciting recipes from around the world. Users can share their own recipes, create virtual cooking classes, and connect with fellow food enthusiasts.", "App", user1.about_me)

    user2 = Account("alice_smith", "p@ssw0rd", "Alice Smith", "alice.smith@example.com", "Front-end developer with a strong background in UI/UX design. Proficient in JavaScript, React, and CSS.", "A partner to bring fresh ideas and creativity to the table.")
    pitch2 = user2.create_pitch("Artify", "An app that brings art lovers together. Users can explore and share their favorite artworks, connect with local artists, and participate in virtual art events.", "App", user2.about_me)
    pitch6 = user2.create_pitch("BookSwap", "A platform for book lovers to exchange and trade books with others who share similar literary interests. Users can create book clubs, participate in virtual book discussions, and discover new reads.", "Website", user2.about_me)

    user3 = Account("sam_jones", "secret123", "Sam Jones", "sam.jones@example.com", "Full-stack developer with experience in building scalable and robust applications. Skilled in Python, Django, and Vue.js.", "A collaborator to turn exciting ideas into successful projects.")
    pitch3 = user3.create_pitch("FitConnect", "A fitness community platform that connects users with similar fitness goals. Users can join challenges, share workout routines, and motivate each other to stay active.", "App", user3.about_me)
    pitch7 = user3.create_pitch("CodeCollab", "An online coding collaboration platform that connects developers from different backgrounds to work on open-source projects. Users can showcase their coding skills, contribute to projects, and learn from each other.", "Software/Website", user3.about_me)

    user4 = Account("emily_wang", "letmein", "Emily Wang", "emily.wang@example.com", "Data scientist with expertise in machine learning and statistical analysis. Worked on projects related to predictive modeling and data-driven decision-making.", "A partner interested in applying machine learning to real-world problems.")
    pitch4 = user4.create_pitch("HealthBot", "An AI-powered health assistant that provides personalized health recommendations based on user data and preferences.", "Software/Webiste", user4.about_me)
    pitch8 = user4.create_pitch("LanguagePal", "An app designed to help users learn new languages through interactive lessons, quizzes, and real-time conversations with native speakers. Connect with language learners globally and enhance your language skills together.", "App", user4.about_me)

    user5 = Account("david_miller", "securepwd", "David Miller", "david.miller@example.com", "Experienced cybersecurity specialist with a focus on threat detection and incident response. Skilled in ethical hacking and penetration testing.", "A partner interested in developing tools and solutions to enhance online security.")
    pitch9 = user5.create_pitch("SecureChat", "A secure messaging app that prioritizes user privacy. Utilizes end-to-end encryption and advanced security features to protect users' conversations from unauthorized access.", "Software/App", user5.about_me)

    user6 = Account("olivia_garcia", "pass123", "Olivia Garcia", "olivia.garcia@example.com", "Graphic designer with a keen eye for aesthetics and a passion for creating visually stunning designs. Proficient in Adobe Creative Suite.", "A collaborator to bring creative design ideas to life and build visually appealing digital experiences.")
    pitch10 = user6.create_pitch("DesignHub", "An online platform for graphic designers to showcase their portfolios, connect with potential clients, and collaborate on design projects.", "Website", user6.about_me)

    user7 = Account("ryan_carter", "ryan123", "Ryan Carter", "ryan.carter@example.com", "Experienced project manager with a track record of leading successful software development projects. Skilled in Agile methodologies and team collaboration.", "A partner with technical skills to co-found a startup and bring innovative tech solutions to the market.")
    pitch11 = user7.create_pitch("ProjectSync", "A project management tool that streamlines collaboration and communication within development teams. Features include task tracking, sprint planning, and real-time project updates.", "Software", user7.about_me)

    user8 = Account("sophie_jackson", "sophiepw", "Sophie Jackson", "sophie.jackson@example.com", "Marketing specialist with expertise in digital marketing, content creation, and social media management. Passionate about building brand awareness.", "A tech-savvy partner to launch a tech-driven marketing solution.")
    pitch12 = user8.create_pitch("SocialBoost", "An AI-powered social media marketing platform that analyzes user engagement data to optimize marketing strategies. Helps businesses increase their online presence and connect with their target audience.", "Online Interface", user8.about_me)


    manager.account_db.accounts = [user1, user2, user3, user4, user5, user6, user7, user8, user]
    manager.account_db.usernames = {"john_doe": user1, "alice_smith": user2, "same_jones": user3, "emily_wang": user4, "mwalsh": user, "david_miller": user5, "olivia_garcia": user6, "ryan_carter": user7, "sophie_jackson": user8}

    manager.pitch_db.pitches = [pitch1, pitch2, pitch3, pitch4, pitch5, pitch6, pitch7, pitch8, pitch9, pitch10, pitch11, pitch12, pitch00, pitch000]

    return manager

# def random_match(account):
    
#     random_pitch = np.random.choice(manager.pitch_db.pitches)

#     return random_pitch

# while True:
#     p = random_match(user4)
#     while p.account == user4:
#         p = random_match(user4)
#     p.display_pitch()
#     prompt = input("Type L to like, D to dislike, or Q to quit:")
#     if prompt == "L":
#        user4.liked_pitches.append(p)
#        p.likes += 1
#     if prompt == "D":
#         p.dislikes += 1
#     if prompt == "Q":
#         break