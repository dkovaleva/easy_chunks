        $(document).ready(function(){
            $('.card-body').on('click', '.chunk-badge', function(){
                var url = $(this).attr('url');
                $('#edit_chunk').show();
                $('#edit_chunk .loading_container').show();
                $.get(url, function(data){
                     $('#edit_chunk .modal-body').html(data);
                     $('#edit_chunk .loading_container').hide();
                });
            });
            $('#edit_chunk').on('click', '.close-modal', function(){
                $('#edit_chunk').hide();
            });
            $('#edit_chunk').on('click', '.submit-form', function(){
                $('#edit_chunk .loading_container').show();
                var post_data = $('#edit_chunk_form').serialize();
                var url = $('#edit_chunk_form').attr('url');
                var chunk_id = $('#edit_chunk_form').attr('chunk_id');
                var edited_chunk = $('#chunk_id_' + chunk_id);
                $.post(url, post_data, function(data){
                    if (data.result == 'ok'){
                        edited_chunk.html(data.text);
                        $('#edit_chunk').hide();
                    } else {
                        $('#edit_chunk_form .error').html(data.error_text);
                    }
                    $('#edit_chunk .loading_container').hide();
                });
            });
        });