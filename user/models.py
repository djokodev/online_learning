from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # ici nous implementons les champs commun a tous les utilisateurs
    username = models.CharField(max_length=60, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    
    profile_picture = models.ImageField(upload_to='profile_pictures', blank=True) 
    """blank=True nous permet de creer un utilisateur sans etre obliger de mettre une photo de profile,
        et profile_pictures quant a lui sert a specifie le chemin vers le quel les photos mis sur
        le site par les utilisateur seront stockés. La valeur peut être une chaîne de caractères qui représente
        un chemin relatif par rapport au répertoire de stockage des fichiers de médias de votre projet Django."""
    
    country_residence = models.CharField(max_length=100)
    
    ENSEIGNANT = "ENSEIGNANT"
    ETUDIANT = "ETUDIANT"
    
    ROLE_CHOICES = (
        (ENSEIGNANT, "Enseignant"),
        (ETUDIANT, "Etudiant"),
    )
    
    status = models.CharField(max_length=30, choices=ROLE_CHOICES, verbose_name='Status')
    """permet de vérifier la valeur du champ  status sans écrire la valeur en dur. 
        Par exemple, si user.status == user.CREATOR"""
    
    class Meta:
        verbose_name = "Utilisateur"
        verbose_name_plural = "utilisateurs" 
        """Ici, verbose_name est défini comme "Utilisateur" et verbose_name_plural comme "Utilisateurs".
            Ces options permettent de personnaliser la façon dont le modèle CustomUsersera affiché dans l'interface
            d'administration de Django et dans d'autres parties de l'application."""
    



class Etudiant(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    """ le champ user veut tout simplement dire que la classe etudiant ne peut avoir qu'une seule 
        instance de la classe CustomUser.. par exemple si un etudiant deja inscrit essaie de se cree un
        autre compte cela seras impossible s'il renseigne les meme valeur au niveau de son username et email"""
        
    registered_course = models.ManyToManyField('course.Course', related_name='etudiants_inscrits')
    """" related_name='etudiants_inscrits' spécifie le nom de la relation inverse, ce qui signifie que 
    vous pouvez accéder aux étudiants inscrits à un cours en utilisant cours_instance.etudiants_inscrits.all() """
    
    note = models.IntegerField(default=0)
    
    def __str__(self):
        return self.user.username



class Enseignant(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    course_taught = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    description = models.TextField()
    
    def __str__(self):
        return self.user.username
    """ cette méthode est utilisée pour obtenir une représentation lisible de l'objet Enseignant.
        dans notre cas quand un objet endeignant sera cree, dans la bd c'est son username qui sera affiche! """