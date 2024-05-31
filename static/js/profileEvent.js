document.addEventListener('DOMContentLoaded', function () {
    const viewAllBtn = document.querySelector('.view-all');

    const allViewBtn = document.querySelector('.allViewBtn');
    const allIcon = document.querySelector('.allViewBtn img');

    const introContainer = document.querySelector('.introView');

    const postViewBtn = document.querySelector('.postViewBtn');
    const postIcon = document.querySelector('.postViewBtn img');
    const postContainer = document.querySelector('.postView');

    const commentViewBtn = document.querySelector('.commentViewBtn');
    const commentIcon = document.querySelector('.commentViewBtn img');
    const commentContainer = document.querySelector('.commentView');

    const likeBtn = document.querySelector('.likeBtn');
    const likeIcon = document.querySelector('.likeBtn img');
    const likeContainer = document.querySelector('.likeView');

    const scrapBtn = document.querySelector('.scrapBtn');
    const scrapIcon = document.querySelector('.scrapBtn img');
    const scrapContainer = document.querySelector('.scrapView');

    function resetStyles() {
        introContainer.style.display = 'none';

        allViewBtn.style.color = '';
        allIcon.style.filter = '';

        postViewBtn.style.color = '';
        postIcon.style.filter = '';
        postContainer.style.display = 'none';
        postContainer.querySelector('.view-all').style.display = 'none';

        commentViewBtn.style.color = '';
        commentIcon.style.filter = '';
        commentContainer.style.display = 'none';
        commentContainer.querySelector('.view-all').style.display = 'none';

        likeBtn.style.color = '';
        likeIcon.style.filter = '';
        likeContainer.style.display = 'none';
        likeContainer.querySelector('.view-all').style.display = 'none';

        scrapBtn.style.color = '';
        scrapIcon.style.filter = '';
        scrapContainer.style.display = 'none';
        scrapContainer.querySelector('.view-all').style.display = 'none';
    }

    allViewBtn.addEventListener('click', function () {
        resetStyles();

        introContainer.style.display = 'block';
        postContainer.style.display = 'block';
        commentContainer.style.display = 'block';
        likeContainer.style.display = 'block';
        scrapContainer.style.display = 'block';

        postContainer.querySelector('.view-all').style.display = 'block';
        commentContainer.querySelector('.view-all').style.display = 'block';
        likeContainer.querySelector('.view-all').style.display = 'block';
        scrapContainer.querySelector('.view-all').style.display = 'block';

        allViewBtn.style.color = 'rgb(209, 24, 24)';
        allIcon.style.filter = 'invert(18%) sepia(94%) saturate(2732%) hue-rotate(352deg) brightness(92%) contrast(95%)';
    });

    postViewBtn.addEventListener('click', function () {
        resetStyles();

        viewAllBtn.style.display = 'none';
        postViewBtn.style.color = 'rgb(209, 24, 24)';
        postIcon.style.filter = 'invert(18%) sepia(94%) saturate(2732%) hue-rotate(352deg) brightness(92%) contrast(95%)';
        postContainer.style.display = 'block';
    });

    commentViewBtn.addEventListener('click', function () {
        resetStyles();

        viewAllBtn.style.display = 'none';
        commentViewBtn.style.color = 'rgb(209, 24, 24)';
        commentIcon.style.filter = 'invert(18%) sepia(94%) saturate(2732%) hue-rotate(352deg) brightness(92%) contrast(95%)';
        commentContainer.style.display = 'block';
    });

    likeBtn.addEventListener('click', function () {
        resetStyles();

        viewAllBtn.style.display = 'none';
        likeBtn.style.color = 'rgb(209, 24, 24)';
        likeIcon.style.filter = 'invert(18%) sepia(94%) saturate(2732%) hue-rotate(352deg) brightness(92%) contrast(95%)';
        likeContainer.style.display = 'block';
    });

    scrapBtn.addEventListener('click', function () {
        resetStyles();

        viewAllBtn.style.display = 'none';
        scrapBtn.style.color = 'rgb(209, 24, 24)';
        scrapIcon.style.filter = 'invert(18%) sepia(94%) saturate(2732%) hue-rotate(352deg) brightness(92%) contrast(95%)';
        scrapContainer.style.display = 'block';
    });
});