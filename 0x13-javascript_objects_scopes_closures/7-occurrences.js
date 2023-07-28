#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  /**
   * function that counts the occurrence of an element inside a list.
   * @list: the list to search the occurrence of the searchElement.
   * @searchElement: the element to search for.
   *
   * Return: The number of occurrence of the element.
   */
  let count = 0;

  for (let i = 0; i < list.length; i++) {
    if (searchElement === list[i]) {
      count++;
    }
  }
  return (count);
};
