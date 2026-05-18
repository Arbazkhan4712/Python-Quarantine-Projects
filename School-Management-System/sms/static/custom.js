$(document).ready(function(){
    $(".count_btn").on("click", function(){
        var btn_property = $(this)
        var row = $(this).closest("tr");
        var admission_number = row.find(".cls_admission").text();
        var admission_class = row.find(".cls_class").text();
//        console.log(admission_number, admission_class);
        var attendance_count_url = 'http://localhost:8000/api/attendance/'+ admission_class + '/' + admission_number
//        console.log(url);

        $.ajax({
            url: attendance_count_url,
            method: 'get',
            success: function(data){
                btn_property.addClass('btn btn-success');
            },
            error: function(err){
                alert("Attendance has already taken")
            }
        });

    })
})

