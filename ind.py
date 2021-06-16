<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=
    , initial-scale=1.0">
    <link rel="stylesheet" href="{% static 'medica/css/index.css' %}">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.11.2/css/all.css">
    
    <title>Médica</title>
    <script
    src="https://code.jquery.com/jquery-3.4.1.slim.min.js"
    integrity="sha256-pasqAKBDmFT4eHoN2ndd6lN370kFiGUFyTiUHWhU7k8="
    crossorigin="anonymous"></script>
    <script>
    $(function() {
    $(".toggle").on("click", function() {
        if ($(".item").hasClass("active")) {
            $(".item").removeClass("active");
        } else {
            $(".item").addClass("active");
        }
    });
});
    </script>
    <link rel="stylesheet" href="http://fonts.googleapis.com/cs?family=karla">
</head>
<body>
 
  <nav>
    <ul class="menu">
      <li class="logo"><a href="#"><img src="{% static 'medica/image/Logos.gif' %}" alt="logo" width="100" height="50" id="logo"></a></li>
        <li class="item"><a href="index.html">Accueil</a></li>
        <li class="item"><a href="#QSN">Qui sommes-nous? </a></li>
        <li class="item"><a href="#NS">Nos services</a></li>
        </li>
        <li class="item button"><a href="#connecter">connecter</a></li>
        <li class="item button secondary"><a href="{% url 'medica/formulaire' %}">S'inscrire</a></li>
        <li class="toggle"><span class="bars"></span></li>
    </ul>
</nav>

  <div class="slider" id="NS">
  <!-- fade css -->
  <div class="myslide fade">
    <div class="txt">
      <h1> services</h1>
      <p>MEDICA est une équipe de médecins et d'infirmiers,<br> présente sur le web qui veille sur la santé et le bien être de ses patients.</p>
    </div class="slide">
    <img src="{% static 'medica/image/1.png' %}" style="width: 100%; height: 100%;" class="img">
  </div>
  
  <div class="myslide fade">
    <div class="txt">
      <h1>Nos services</h1>
      <p>Avec MEDICA vous pouvez consulter nos médecins et <br>
        bénéficier d'un suivi médical complet à parir de votre maison gratuitement !</p>
    </div >
    <img src="{% static 'medica/image/2.png' %} " style="width: 100%; height: 100%;" class="img">
  </div>
  
  <div class="myslide fade">
    <div class="txt">
      <h1>Nos services</h1>
      <p>Notre équipe est passionnée et nous nous engageons à fournir à nos clients <br>
         des solutions Web sur mesures conçues pour vous aider à établir une presence en ligne</p>
    </div >
    <img src="{% static 'medica/image/3.png' %}" style="width: 100%; height: 100%;" class="img">
  </div>
  
  <div class="myslide fade">
    <div class="txt">
      <h1>Nos services</h1>
      <p> Et optimiser la communication de votre cabinet ou <br> 
        votre clinique médicale quelle que soit votre spécialité.</p>
    </div> 
    <img src="{% static 'medica/image/4.png' %}" style="width: 100%; height: 100%;" class="img">
  </div>
  
  <div class="myslide fade">
    <div class="txt">
      <h1>Nos services</h1>
      <p>Vous vivez avec vos grands parents? L'un des deux a subi un malaise ? <br>
      L' hopital est loin de chez vous ? Ne vous inquiétez surtout pas !
     <br> Contactez nous, MEDICA répondra diréctement à votre urgence .
     <br> Avec MEDICA soyez tranquille</p>
    </div>
    <img src="{% static 'medica/image/5.png' %}" style="width: 100%; height: 100%;" class="img">
  </div>
  <!-- /fade css -->
  
  <!-- onclick js -->
  <a class="prev" onclick="plusSlides(-1)">&#10094;</a>
    <a class="next" onclick="plusSlides(1)">&#10095;</a>
  
  <div class="dotsbox" style="text-align:center">
    <span class="dot" onclick="currentSlide(1)"></span>
    <span class="dot" onclick="currentSlide(2)"></span>
    <span class="dot" onclick="currentSlide(3)"></span>
    <span class="dot" onclick="currentSlide(4)"></span>
    <span class="dot" onclick="currentSlide(5)"></span>
  </div>
  <!-- /onclick js -->
</div>

<script src="{% static 'medica/js/index.js' %}"></script>
<!---/Qui sommes nous?-->
<div class="container" id="QSN">
  <div class="header">
    <h1>Qui sommes-nous?</h1>
    <div class="sb-container">
    <div class="teams">
      <img src="{% static 'medica/image/profile.jpg' %}" alt="image">
      <div class="name">Allam Imane</div>
      <div class="design">Etudiante</div>
      <div class="about"><p>Etudiante en 3 ème année informatique. <br>Sécialité: système d'information. </p>
      </div>
    </div>
    <div class="teams">
      <img src="{% static 'medica/image/profile.jpg' %}" alt="image">
      <div class="name">Meshoul Lyna Rayane</div>
      <div class="design"> Etudiante</div>
      <div class="about"><p>Etudiante en 3ème année informatique. <br> Spécialité: système d'information. </p>
        </div>
    </div>
    <div class="teams">
      <img src="{% static 'medica/image/profile.jpg' %}" alt="image">
      <div class="name">Benhizia malak Belkisse</div>
      <div class="design">Etudiante</div>
      <div class="about"><p>Etudiante en 3 ème année informatique. <br> Spécialité: système d'information. </p>
       </div>
    </div>
  </div>
  </div>
  
</div> 

<!--- connecter--->

<section  id="connecter" >
  <div class="imgBx" >
    <img src="{% static 'medica/image/login.png' %}" alt=""> </div>
    <div class="contentBX">
      <div class="formBx">
        <h2>Se connecter</h2>
        <form action="">

          <div class="inputBx">
            <span>Email</span>
            <input type="email">
          </div>
          <div class="inputBx">
            <span>Mot de passe</span>
            <input type="password">
          </div>
          <div class="remember">
            <label for=""> 
              <input type="checkbox" name="">Remember me
            </label></div>
            <div class="inputBx">
              <input type="submit" value="Se connecter">
            </div>
            <div class="inputBx">
              <p>Avez-vous un compte dèjà? <a href="formulaire.html">  S'inscrire</a></p>
            </div>

         
          
        </form>
      </div>

    
</div>
</section>
<!---feedback section-->


<!-----circular progress -->

  

<!---footer-->
  
<footer>
  <div class="footer-container">
    <div class="left-col">
      
      <div class="social-media">
        <a href="#"><i class="fab fa-facebook-f"></i></a>
        <a href="#"><i class="fab fa-twitter"></i></a>
        <a href="#"><i class="fab fa-instagram"></i></a>
        <a href="#"><i class="fab fa-linkedin-in"></i></a>
      </div>
      <p class="rights-text">© Université Abdelhamid Mehri - Constantine 2. Tous les droits sont réservés.</p><br>
      <p class="rights-text">Email : Médica@gmail.com</p>
      
    </div>

    <div class="right-col">
      <h1>Nous vous remercions pour votre confiance</h1>
      <div class="border"></div>
      <p class ="rights-text" >Entrez votre e-mail pour obtenir nos nouvelles et mises à jour.</p>
      <form action="" class="newsletter-form">
        <input type="text" class="txtb" placeholder="Entrez votre email">
        <input type="submit" class="btn" value="Envoyer">
      </form>
    </div>
  </div>
</footer>
  
</body>
</html>
