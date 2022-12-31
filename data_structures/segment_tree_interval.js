let intervals = null
let tree = null
let yOff = 0
const yStep = 10
let nIntervals = 0

function Node(b, e) {
    this.b = b
    this.e = e
    this.left = null
    this.right = null
    this.key = 0
    this.aux = []
}

function Endpoint(v, ix) {
    this.v = v
    this.ix = ix
}

function buildSegmentTree(intervals) {
    let tree = {}

    _build = (s, t) => {
        var v = new Node(s, t)
        if (s+1 == t) { return v }
        const m = Math.floor((s+t)/2)
        v.key = m
        v.left = _build(s, m)
        v.right = _build(m, t)
        return v
    }

    eps = []
    for (const [ix, [start, end]] of intervals.entries()) {
        eps.push(new Endpoint(start, ix))
        eps.push(new Endpoint(end, ix))
    }
    eps.sort((a, b) => a.v - b.v)
    let root = _build(0, eps.length-1)

    _insert = (v, b, e) => {
        if ((b <= v.b) && (v.e <= e)) {
            v.aux.push([eps[b].v, eps[e].v, eps[b].ix])
            return
        }
        if (b < v.key) { _insert(v.left, b, e) }
        if (v.key < e) { _insert(v.right, b, e) }
    }

    var seen = {}
    for (const [i, ep] of eps.entries()) {
        if (seen[ep.ix] === undefined) { seen[ep.ix] = i }
        else { _insert(root, seen[ep.ix], i) }
    }

    _extend = (out, values) => { for (const v of values) { out.add(v) } }
    var numVisited = 0
    _query = (v, q) => {
        numVisited += 1
        var out = new Set()
        if (!v) { return out }
        if ((eps[v.b].v <= q) && (q <= eps[v.e].v)) { _extend(out, v.aux) }
        if (q <= eps[v.key].v) { _extend(out, _query(v.left, q)) }
        if (q >= eps[v.key].v) { _extend(out, _query(v.right, q)) }
        return out
    }

    tree.query = q => {
        numVisited = 0
        return [Array.from(_query(root, q)), numVisited]
    }
    return tree
}

function randomIntervals(n) {
    let intervals = [];
    for (let i = 0; i < n; i++) {
        let start = random(0, windowWidth)
        let end = start + random(0, (windowWidth - start) / 2)
        intervals.push([start, end, i])
    }
    return intervals;
}

function setup() {
    //randomSeed(0)
    yOff = 300
    nIntervals = Math.floor((windowHeight - yOff) / (yStep))
    intervals = randomIntervals(nIntervals)
    tree = buildSegmentTree(intervals)

    createCanvas(windowWidth,windowHeight)
    background(255)
}

function drawIntervals(intervals, color) {
    drawingContext.setLineDash([10, 0])
    for (const [l, r, ix] of intervals) {
        fill(color)
        stroke(color)
        // line(l, yOff+yStep*ix, r, yOff+yStep*ix)
        rect(l, yOff+yStep*ix, r-l, 5)
    }
}

function drawCursor() {
    drawingContext.setLineDash([2, 20])
    background(255)
    stroke(color(0, 100, 0))
    line(mouseX, 0, mouseX, height)
}

function draw() {
    drawCursor()
    drawIntervals(intervals, color(0, 0, 0))
    const [ivs, n] = tree.query(mouseX)
    drawIntervals(ivs, color(255, 0, 0))

    fill(0)
    stroke(0)
    textSize(32)
    const label = `${n}/${intervals.length}`
    text(label, 10, 30)
}
