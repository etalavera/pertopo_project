var PROJECT_ID;
var ESTIMATE_METERS;
var TOTAL_METERS;

function setRowId(id, name) {
    PROJECT_ID = id;
    PROJECT_TITLE = name;
    show_tables('id_project_sections');
}

function editRow(id) {
  // Get Logbook row
}

function show_tables(c) {
  switch (c) {
    case 'id_project_sections':
      $("#id_projects_main").css("display", "none");
      fillLogbookTable();
      $("#id_project_sections").css("display", "block");
      break;
    case 'id_projects_main':
      fillProjectTable();
    default:

  }
}

function fillProjectTable() {
  ///
  /// Llenar los datos de la tabla de proyectos.
  /// esta función consume el API: apiConsultas.

  //loading("show")

  $.ajax({
    method:'GET',
    url:'/apiConsultas/query_projects',
    success: function (response) {
      var cont = 0;
      var parseJson = JSON.parse(response);
      console.log("Respuesta fillProjectTable");
      console.log(parseJson);

      for(var i=0; i<parseJson.length; i++) {
        cont = cont + 1;
        var nameToSting = "'"+ parseJson[i].fields.project_name.toString() + "'";
        $("#id_projects_table").find('tbody').append(''+
          '<tr onclick="setRowId('+ parseJson[i].pk +', '+nameToSting+')">' +
            '<td><a href="#">'+ cont +'<a/></td>'+
            '<td><a href="#">'+ parseJson[i].fields.project_name +'</a></td>' +
            '<td><a href="#">'+ parseJson[i].fields.project_leader +'</a></td>' +
            '<td><span class="badge bg-danger">'+ parseJson[i].fields.project_progress +' %</span></td>' +
          '</tr>'
        );
      }
    },
    error: function (x, t, m) {
      alert("fillProjectTable error: " + x);
    }
  });
}

function fillLogbookTable() {
  ///
  /// Llenar la tabla de bitacoras del proyecto.
  /// Esta función se ejecuta al dar click sobre un elemento de la
  /// tabla de proyectos.

  //loading();
  console.log("Respuesta fillLogbookTable: ");
  $.ajax({
    method: 'GET',
    url: '/apiConsultas/query_logbook',
    data: {project_id:PROJECT_ID},
    success: function (response) {

      console.log(response);
      if (response == '[]') {
        console.log("No se encontraron registros");
      }
      else {

        var cont = 0;
        response = JSON.parse(response);
        console.log(response);
        // setear el nombre del proyecto
        $('#id_project_title').html("Proyecto: " + PROJECT_TITLE)
        // sacar metros totales
        TOTAL_METERS = 0;
        for(var i=0; i<response.length; i++) {
          log_meters = parseFloat(response[i].fields.log_meters);
          TOTAL_METERS = TOTAL_METERS + log_meters;
        }

        $('#id_total_meters').html('<i class="fa fa-caret-left"></i>'+ TOTAL_METERS)
        $('#id_logbook_table').find('tbody').html(""); // limpiar la tabla antes de mostrar
        for(var i=0; i<response.length; i++) {
          cont = cont + 1;

          $('#id_logbook_table').find('tbody').append(''+
            '<tr onclick="editRow('+response[i].pk+')">'+
              '<td>'+cont+'</td>'+
              '<td>'+response[i].fields.log_date+'</td>'+
              '<td>'+response[i].fields.log_meters+'</td>'+
              '<td>'+response[i].fields.log_task+'</td>'+
            '</tr>'
          );
        }
      }

    },
    error: function (x, t, m) {
      alert("Errror");
    }
  });
}
