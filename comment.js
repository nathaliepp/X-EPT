document.getElementById('form-comment').addEventListener('submit', savecomment);

function savecomment(e) {
  let name = document.getElementById('name').value;  

  let description = document.getElementById('description').value;
  console.log(description)
  
  let comment = {
    name,
    description
  };

  if(localStorage.getItem('comments') === null) {
    let comments = [];
    comments.push(comment);
    localStorage.setItem('comments', JSON.stringify(comments));
  } else {
    let comments = JSON.parse(localStorage.getItem('comments'));
    comments.push(comment);
    localStorage.setItem('comments', JSON.stringify(comments));
  }

  getcomments();
  document.getElementById('form-comment').reset();
  e.preventDefault();
}

function deletecomment(name) {
  console.log(name)
  let comments = JSON.parse(localStorage.getItem('comments'));
  for(let i = 0; i < comments.length; i++) {
    if(comments[i].name == name) {
      comments.splice(i, 1);
    }
  }

  localStorage.setItem('comments', JSON.stringify(comments));
  getcomments();
}

function getcomments() {
  let comments = JSON.parse(localStorage.getItem('comments'));
  let commentsView = document.getElementById('comments');
  commentsView.innerHTML = '';
  for(let i = 0; i < comments.length; i++) {
    let name = comments[i].name;
    let description = comments[i].description;

    commentsView.innerHTML += `<div class="card mb-3">
        <div class="card-body">
            <a onclick="deletecomment('${name}')" ><i class="fab flaticon-user-inside-bubble-speech"></i></a>
            <p>${name} - ${description}</p>
        </div>
      </div>`;
  }
}

getcomments();



