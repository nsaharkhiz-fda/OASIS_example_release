

$.fn.DataTable.ext.pager.numbers_length = 10;

$(document).ready(function () {
    $.getJSON("metadata.json").done(function (data) {
        $.each(data, function (idx, e) {
            artifact = "none";
            if (e['frame']) artifact = "frame";
            else if (e['calibration_chart']) artifact = "chart";
            else if (e['ruler']) artifact = "ruler";
            $('#ssynth-table').append(
            `<tr id="ssynth-${idx}" >
                <td>${e['skin']}</td>
                <td>${e['hair']}</td>
                <td>${e['melatonin']}</td>
                <td>${e['blood']}</td>
                <td>${e['lesion']}</td>
                <td>${e['timepoint']}</td>
                <td>${e['material']}</td>
                <td>${e['hair_albedo']}</td>
                <td>${e['lighting']}</td>
                <td>${e['camera_distance']}</td>
                <td>${artifact}</td>
                <td><a href="images/${e["filename"]}"><img src="images/${e["filename"]}" width="50"></a></td>
            </tr>`);
        });
        
        let table = new DataTable('#ssynth-table',
            {
                order: [[0, 'asc']],
                layout: {
                    
                    topStart: 'info',
                    bottom: 'paging',
                    bottomStart: null,
                    bottomEnd: null
                },                
                initComplete: function () {
                    this.api()
                        .columns()
                        .every(function () {
                            let column = this;

                            if(column.type()=="html-num"){
                                column.footer().replaceChildren("");
                                return;
                            }
                            let title = column.footer().textContent;
             
                            // Create input element
                            let input = document.createElement('input');
                            input.className="footer-search";
                            input.placeholder = title;
                            column.footer().replaceChildren(input);
             
                            // Event listener for user input
                            input.addEventListener('keyup', () => {
                                if (column.search() !== this.value) {
                                    column.search(input.value).draw();
                                }
                            });
                        });
                }
            }
        );
        Fancybox.bind('img', {
            //
          }); 
    });
});