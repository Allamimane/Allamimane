<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="utf-8">
    
    <title>profile </title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
	<script src="https://code.jquery.com/jquery-1.10.2.min.js"></script>
	<link rel="stylesheet" href="patient.css">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.0/dist/css/bootstrap.min.css" rel="stylesheet">
	<script src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.0/dist/js/bootstrap.bundle.min.js"></script>
	<script src="https://kit.fontawesome.com/6d5f8ea701.js" crossorigin="anonymous"></script>
</head>
<body>
<div class="container">
		<div class="main-body">
			<div class="row">
				<div class="col-lg-4">
					<div class="card">
						<div class="card-body">
							<div class="d-flex flex-column align-items-center text-center">
								<img src="image/prof.jpg" alt="Admin" class="rounded-circle p-1 bg-info" width="110" >
								<div class="mt-3">
									<h4 >Profile </h4>
									<p class="text-secondary mb-1">Bienvenue</p>
									<button class="btn btn-info" herf ="index.html">Accueil</button>
									<button class="btn btn-outline-info">Déconnecter</button>
									
								</div>
							</div>
							<hr class="my-4">
							<div class="side-nav">
								<h2 >General</h2>
								<nav>
									<ul>
										<li class="active" onclick="show(0)">
										<span><i class="fa fas fa-tachometer"> <a href="infermier.html"></a></i></span>
										<h3>My Profile</h3>
									</li>
									<li  onclick="show(1)">
										<span><i class="fas fa-star"></i></span>
										<h3>Notifications</h3>
									</li>
									<li  onclick="show(2)">
										<span><i class="fas fa-cog"></i></span>
										<h3>Faire des soins</h3>
									</li>
									<li  onclick="show(3)">
										<span><i class=" far fa-comment"></i></span>
										<h3>Messagerie</h3>
									</li>
									</ul>
								</nav>

							</div>
						</div>
					</div>
				</div>
				<div class="col-lg-8">
					<div class="card">
						<div class="card-body">
							<div class="row mb-3">
								<div class="col-sm-3">
									<h6 class="mb-0">Nom et prénom</h6>
								</div>
								<div class="col-sm-9 text-secondary">
									<input type="text" class="form-control" value="" placeholder="benizin kader ">
								</div>
							</div>
							<div class="row mb-3">
								<div class="col-sm-3">
									<h6 class="mb-0">Email</h6>
								</div>
								<div class="col-sm-9 text-secondary">
									<input type="email" class="form-control" value="" placeholder="xample@gmail.com">
								</div>
							</div>
							<div class="row mb-3">
								<div class="col-sm-3">
									<h6 class="mb-0">TéléPhone</h6>
								</div>
								<div class="col-sm-9 text-secondary">
									<input type="text" class="form-control" value="" placeholder="05 55 30 66 88 ">
								</div>
							</div>
							<div class="row mb-3">
								<div class="col-sm-3">
									<h6 class="mb-0">Age</h6>
								</div>
								<div class="col-sm-9 text-secondary">
									<input type="text" class="form-control" value="" placeholder="25">
								</div>
							</div>
							<div class="row mb-3">
								<div class="col-sm-3">
									<h6 class="mb-0">Adresse</h6>
								</div>
								<div class="col-sm-9 text-secondary">
									<input type="text" class="form-control" value="" placeholder="nouvelle ville uv-17">
								</div>
							</div>
							<div class="row">
								<div class="col-sm-3"></div>
								<div class="col-sm-9 text-secondary">
									<input type="button" class="btn btn-info px-4" value="Sauvegarder les modifications">
								</div>
							</div>
						</div>
					</div>
					<div class="row">
						<div class="col-sm-12">
							<div class="card">
								<div class="card-body">
									<h5 class="d-flex align-items-center mb-3"></h5>
									<p>Femme</p>
									<div class="progress mb-3" style="height: 5px">
										<div class="progress-bar bg-info" role="progressbar" style="width: 80%" aria-valuenow="80" aria-valuemin="0" aria-valuemax="100"></div>
									</div>
									<p>Homme</p>
									<div class="progress mb-3" style="height: 5px">
										<div class="progress-bar bg-danger" role="progressbar" style="width: 72%" aria-valuenow="72" aria-valuemin="0" aria-valuemax="100"></div>
									</div>
									<p>Qualité</p>
									<div class="progress mb-3" style="height: 5px">
										<div class="progress-bar bg-success" role="progressbar" style="width: 89%" aria-valuenow="89" aria-valuemin="0" aria-valuemax="100"></div>
									</div>
									
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>

<style type="text/css">
body{
    background: #03989e;
    margin-top:20px;
}
.card {
    position: relative;
    display: flex;
    flex-direction: column;
    min-width: 0;
    word-wrap: break-word;
    background-color: #d5dbd9;
    background-clip: border-box;
    border: 0 solid transparent;
    border-radius: .25rem;
    margin-bottom: 1.5rem;
    box-shadow: 0 2px 6px 0 rgb(218 218 253 / 65%), 0 2px 6px 0 rgb(206 206 238 / 54%);
}
.me-2 {
    margin-right: .5rem!important;
}
</style>

<script type="text/javascript">

</script>
</body>
</html>
