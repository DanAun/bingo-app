function setup(playerName) {
    document.querySelectorAll('.cell').forEach(cell => {
        cell.addEventListener('click', () => {
            const index = parseInt(cell.dataset.index);
            const isMarked = cell.classList.contains('marked');
            const url = `/${playerName}/${isMarked ? 'unmark' : 'mark'}`;
            fetch(url, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ cell_index: index })
            }).then(res => res.json()).then(data => {
                cell.classList.toggle('marked');
            });
        });
    });
}
