#!/usr/bin/node

exports.esrever = function (list) {
  /**
   * function that reverses a list.
   * @list: the list to be reversed.
   *
   * Return: the reversed list.
   */
  const reversedList = [];

  for (let i = 1; i <= list.length; i++) {
    reversedList.push(list[list.length - i]);
  }
  return (reversedList);
};
