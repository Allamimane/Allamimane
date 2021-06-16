{% load static %}
<!DOCTYPE html>

<html>
<head>
<title>S'inscrire</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />

<!-- Custom Theme files -->
<link rel="stylesheet" href="{% static 'medica/css/index1.css' %}">
<!-- //Custom Theme files -->
<!-- web font -->
<link href="//fonts.googleapis.com/css?family=Roboto:300,300i,400,400i,700,700i" rel="stylesheet">
<!-- //web font -->
</head>
<body>
	<!-- main -->
<form action="post">
	<div class="wrapper">
		<div class="title">
		  S'inscrire
		</div>
		<div class="form">
		   <div class="inputfield" >
			  <label>Nom</label>
			  <input type="text" class="input" placeholder="MESHOUL">
		   </div>  
			<div class="inputfield">
			  <label>Prénom</label>
			  <input type="text" class="input" placeholder="Lina">
		   </div>  
		   <div class="inputfield">
			  <label>Mot de passe</label>
			  <input type="password" class="input" placeholder=" entrer votre mot de passe">
		   </div>  
		  <div class="inputfield">
			  <label>Confirmer le mot de passe</label>
			  <input type="password" class="input" placeholder="confirmr votre mot de passe">
		   </div> 
			<div class="inputfield">
			  <label>Sexe</label>
			  <div class="custom_select">
				<select>
				  <option value="">Select</option>
				  <option value="male">Homme</option>
				  <option value="female">Femme</option>
				</select>
			  </div>
		   </div> 

		   <div class="inputfield">
			<label  >Date de naissance </label>
			
			 
				
			<input type="date" class="input" >

				
		 </div> 
		 <div class="inputfield">
			<label >Âge</label>
			<input type="number" class="input" placeholder="20">
		 </div> 
			<div class="inputfield">
			  <label>Email Adresse</label>
			  <input type="email" class="input" placeholder ="xample@gmail.com" >
		   </div> 
		  <div class="inputfield">
			  <label>Téléphone</label>
			  <input type="text" class="input" placeholder="05 58 99 66 10">
		   </div> 
		  <div class="inputfield">
			  <label>Adresse</label>
			  <textarea class="textarea" placeholder=" constantine nouvelle ville uv-20"></textarea>
		   </div> 
		  <div class="inputfield">
			<label for="catégorie">Catégorie:</label>
             <div class="catégorie">
			<select name="catégorie">
				<option value="">Select</option>
			  <option value="Patient">Patient</option>
			  <option value="médecin">Médecin</option>
			  <option value="Infirmier ">Infirmier </option>
		
			</select> 
		</div>
		   </div> 
		  <div class="inputfield terms">
			  <label class="check">
				<input type="checkbox">
				<span class="checkmark"></span>
			  </label>
			  <p>Agreed to terms and conditions</p>
		   </div> 
		  <div class="inputfield">
			<input type="submit" value="S'inscrire" class="btn">
		  </div>
		</div>
	</div>
</form>

	<!-- //main -->
</body>
</html>
