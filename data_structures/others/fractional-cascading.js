$(document).ready(function() {

});

function FCNode(value, original = true, indexBelow = null) {
  (this.value = value),
    (this.original = original),
    (this.nextPromoted = null),
    (this.indexBelow = indexBelow);
}

function FCList(listOfValues) {
  this.generateList = function(vals) {
    values = [];
    vals
      .concat()
      .sort(function(a, b) {
        return a - b;
      })
      .forEach(element => {
        values.push(new FCNode(element));
      });
    return values;
  };
  this.values = this.generateList(listOfValues);
  this.cascadeUp = function(FCListAbove) {
    currentIndexOther = 0;
    var tempCopy = FCListAbove.values;
    for (i = 1; i < this.values.length; i += 2) {
      var val = this.values[i].value;
      var insertNode = new FCNode(val, false, i);
      while (
        currentIndexOther < FCListAbove.values.length &&
        FCListAbove.values[currentIndexOther].value <= val
      ) {
        currentIndexOther++;
      }
      tempCopy.splice(currentIndexOther, 0, insertNode);
    }
    FCListAbove.values = tempCopy;
    var lastpromoted = -1;
    for (i = 0; i < FCListAbove.values.length; i++) {
      if (!FCListAbove.values[i].original) {
        for (j = lastpromoted + 1; j < i; j++) {
          FCListAbove.values[j].nextPromoted = i;
        }
        lastpromoted = i;
      }
    }
    for (j = lastpromoted + 1; j < FCListAbove.values.length; j++) {
      FCListAbove.values[j].nextPromoted = lastpromoted;
    }
  };
}

function hitTuple(list, index, found=false) {
  (this.list = list), (this.index = index), (this.found=found);
}

function Search() {
  this.hits = [];
  this.results = [];
  this.driver = function(listOfFCLists, query) {
    var list = listOfFCLists;
    var x = query;
    var result = this.binarySearch(list[0].values, x);
    var binSearchNode = this.hits[this.hits.length - 1].index;
    if (result) {
      this.results.push(true);
    } else {
      if (list[0].values[binSearchNode].value < x){
        binSearchNode = Math.min(binSearchNode+1, list[0].values.length-1)
      }
      this.results.push(false);
    }
    var cursor = binSearchNode

    for (i = 1; i < list.length; i++) {
      if (list[i-1].values[cursor].original) {
        cursor = list[i-1].values[cursor].nextPromoted;
        this.hits.push(new hitTuple(i-1,cursor, false))
      }
      cursor = list[i-1].values[cursor].indexBelow
      
      listHits = []
      listHits.push(new hitTuple(i, cursor, false))
      listHits.push(new hitTuple(i, cursor-1, false))
      if (cursor == list[i].values.length-2){
        listHits.push(new hitTuple(i, cursor+1, false))
      }

      if (list[i].values[cursor].value == x && list[i].values[cursor].original) {
        this.results.push(true)
        listHits[0].found = true
        while(listHits.length != 1) {
          listHits.pop()
        }
      } else if (cursor >= 1 && list[i].values[cursor-1].value >= x) {
        while(listHits.length != 2) {
          listHits.pop()
        }
        if(list[i].values[cursor-1].original && list[i].values[cursor-1].value == x) {
          this.results.push(true)
          listHits[1].found = true
        } else{
          cursor -= 1
          this.results.push(false)
        }
      } else if (cursor == list[i].values.length -2 && list[i].values[cursor].value < x) {
        if (list[i].values[cursor+1].value == x && list[i].values[cursor+1].original) {
          this.results.push(true)
          listHits[2].found = true
        } else {
          this.results.push(false)
          cursor += 1
        }
      } else {
        this.results.push(false)
      }
      listHits.forEach(element => {
        this.hits.push(element)
      })
    }

    return null;
  };

  this.binarySearch = function(arr, x) {
    let start = 0,
      end = arr.length - 1;
    // Iterate while start not meets end
    while (start <= end) {
      // Find the mid index
      let mid = Math.floor((start + end) / 2);
      var hit = new hitTuple(0, mid);
      // If element is present at mid, return True
      if (arr[mid].value == x) {
        if (arr[mid].original) {
          hit.found = true
          this.hits.push(hit);
          return true;
        }
        for (i = 0; i < arr.length; i++) {
          if (arr[i].value == x) {
            if (arr[i].original) {
              this.hits.push(new hitTuple(0,i,true))
              return true;
            }
            this.hits.push(new hitTuple(0, i));
          }
        }
        return false;
      }
      // Else look in left or right half accordingly
      else if (arr[mid].value < x) start = mid + 1;
      else end = mid - 1;
      this.hits.push(hit);
    }
    return false;
  };
}
