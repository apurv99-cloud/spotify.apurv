document.addEventListener("DOMContentLoaded", () => {
    const playButtons = document.querySelectorAll(".play-button");
    const audioPlayer = document.getElementById("audio-player");
    const audioSource = document.getElementById("audio-source");
    const currentSongImage = document.getElementById("current-song-image");

    playButtons.forEach(button => {
        button.addEventListener("click", () => {
            const songDiv = button.closest(".song");
            const songUrl = songDiv.dataset.url;
            const songImage = songDiv.dataset.image;

            // Update audio source and play
            audioSource.src = songUrl;
            currentSongImage.src = songImage;
            audioPlayer.load();
            audioPlayer.play();
        });
    });
});
