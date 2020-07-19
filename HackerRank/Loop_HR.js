main();

function main() {
    nums = ['1','2','4','2','5','3'];
    nums.sort();
    var unique = nums.filter(function(elem, index, self) {
    return index === self.indexOf(elem);
})
            console.log(unique);
}