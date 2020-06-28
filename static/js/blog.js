

document.addEventListener('DOMContentLoaded', function () {
    let s = document.createElement('script');
    s.setAttribute('src', 'https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js');
    document.head.appendChild(s);
    s.onload = () => {
        tinymce.init({
            selector: '#id_desc',  // change this value according to your HTML
          });
          
    }
});
