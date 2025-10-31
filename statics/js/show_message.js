function closeToast(btn) {
    const toast = btn.parentElement;
    toast.classList.remove("show");
    setTimeout(() => toast.remove(), 400);
}

setTimeout(() => {
    document.querySelectorAll(".toast").forEach(toast => {
        toast.classList.remove("show");
        setTimeout(() => toast.remove(), 400);
    });
}, 4000);
