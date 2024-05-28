// 페이지 로드 시 실행되는 함수
$(document).ready(function () {
    // 좋아요 버튼 클릭 이벤트
    // 좋아요 버튼을 누르면 하트 색깔이 채워지며 좋아요 수 +1
    // 또 누르면 원래 모양으로 변하며 좋아요 수 -1
    // !! 좋아요 수 관련은 장고에서 관리하는 것으로 알고 있긴 함.
    // !! 좋아요 수 더하기 관련 jQuery 필요없다면 주석으로 '!!' 해놓은거 다 지우면 됨니당.
    $(".likeBtn i").on("click", function (e) {
        // 이벤트 버블링 막기 : 특정 요소에서 이벤트가 발생했을 때 그 이벤트가 부모 요소로 전파되지 않도록 하는 것을 의미
        // -> i를 클릭해야만 해당 이벤트 발생
        e.stopPropagation();
        var $icon = $(this);
        var $span = $icon.closest(".likeBtn").find("span"); // !!
        var count = parseInt($span.text()); // !!

        if ($icon.hasClass("fa-regular")) {
            $icon.removeClass("fa-regular").addClass("fa-solid");
            $span.text(count + 1); // !!
        } else {
            $icon.removeClass("fa-solid").addClass("fa-regular");
            $span.text(count - 1); // !!
        }
    });

    // 스크랩 버튼 클릭 이벤트
    // 스크랩 버튼을 누르면 별 색깔이 채워짐
    // !! 해당 페이지가 스크랩 목록에 추가되야 함
    $(".scrapBtn i").on("click", function (e) {
        e.stopPropagation();
        var $icon = $(this);

        if ($icon.hasClass("fa-regular")) {
            $icon.removeClass("fa-regular").addClass("fa-solid");
        } else {
            $icon.removeClass("fa-solid").addClass("fa-regular");
        }
    });

    // 댓글 버튼 클릭 이벤트
    // 댓글 버튼 누르면 색깔 채워지며 댓글 창이 보이게 됨
    $('.commentBtn').click(function () {
        // 해당 버튼의 부모 요소에 있는 commentBox를 찾아 토글
        $(this).parent().parent().next('.commentBox').slideToggle();

        // 댓글 버튼 색깔 채우게 함
        $(this).find('i').toggleClass('fa-regular fa-solid fa-comment fa-comment');

        // 다른 댓글 버튼에 대한 처리
        $('.commentBtn').not(this).each(function () {
            // 다른 버튼의 i 요소의 클래스를 변경
            $(this).find('i').removeClass('fa-solid fa-comment').addClass('fa-regular fa-comment');

            // 해당 버튼의 댓글 상자를 닫음
            $(this).parent().parent().next('.commentBox').slideUp();
        });

        // show_comment_create(this.dataset.formUrl, this.data.commentId)
    });

    // 댓글 입력 시 등록 버튼 색상 변경
    $(".commentText").on("input", function () {
        changeButtonColor();
    });
});

// 댓글 입력 시 등록 버튼 색상 변경 함수
function changeButtonColor() {
    var commentContent = $(".commentText").text().trim();
    var submitButton = $(".commentCreateBtn");

    if (commentContent === "") {
        submitButton.css({
            "background-color": "white",
            "color": "rgb(106, 106, 106)"
        });
    } else {
        submitButton.css({
            "background-color": "rgb(183, 84, 79)",
            "color": "white"
        });
    }
}

