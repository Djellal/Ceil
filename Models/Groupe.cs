using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace Ceil.Models
{
    public class Groupe
    {
        [Key]
        [DatabaseGenerated(DatabaseGeneratedOption.Identity)]
        public int Id { get; set; }

        [MaxLength(30)]
        public string GroupeName { get; set; } = "";

        [Required]
        [ForeignKey("Course")]
        public int CourseId { get; set; }
        public Course? Course { get; set; }

        [Required]
        [ForeignKey("CourseLevel")]
        [Display(Name = "Course Level")]
        public int CourseLevelId { get; set; }
        public CourseLevel? CourseLevel { get; set; }

        [Required]
        [ForeignKey("Session")]
        public int SessionId { get; set; }
        public Session? Session { get; set; }
    }
}
