/**
 * Internationalization methods for '2048' game.
 * 
 * @author Igor A. <a4vi2r@gmail.com>
 */

'use strict';

var Localizer = (function(lang) {
	var defaultMsgs = {
		intro : '合并这些数字并最终得到 <strong>2048 数字块!</strong>',
		new_game : '新的一局',
		undo : '撤销',
		keep_going : '继续',
		try_again : '重试',
		ok : 'OK',
		cancel : '取消',
		start_a_new_game : '开始一个新游戏?',
		undo_the_current_move : '撤销当前一步?',
		you_win : '你赢了!',
		game_over : '游戏结束!'
	};

	var localizedMsgs = {};

	this.lang = lang || 'en';

	switch (this.lang) {
	case 'ru':
		localizedMsgs = {
			intro : 'Объединяйте числа и получите <strong>2048!</strong>',
			new_game : 'Новая игра',
			undo : 'Отменить ход',
			keep_going : 'Продолжайте',
			try_again : 'Попробовать ещё раз',
			ok : 'ОК',
			cancel : 'Отмена',
			start_a_new_game : 'Начать новую игру?',
			undo_the_current_move : 'Отменить текущий ход?',
			you_win : 'Вы победили!',
			game_over : 'Игра закончена!'
		};
		break;
	case 'uk':
		localizedMsgs = {
			intro : 'Об\'єднуйте числа і отримаєте <strong>2048!</strong>',
			new_game : 'Нова гра',
			undo : 'Скасувати хід',
			keep_going : 'Продовжуйте',
			try_again : 'Спробувати ще раз',
			ok : 'ОК',
			cancel : 'Відміна',
			start_a_new_game : 'Почати нову гру?',
			undo_the_current_move : 'Скасувати поточний хід?',
			you_win : 'Ви виграли!',
			game_over : 'Гра завершена!'
		};
		break;
	}

	// In Android (ES5 and earlier) we can not use Object.assign method
	this.messages = mergeObjects(defaultMsgs, localizedMsgs);

	/**
	 * Return localized string by key or default english string if key not
	 * found.
	 */
	this.get = function(key) {
		if (typeof this.messages[key] === 'string') {
			return this.messages[key];
		}
		return '';
	};

	return this;
});

/**
 * Overwrites o1's values with o2's and adds o2's if non existent in o1.
 */
function mergeObjects(o1, o2) {
	var r = {};
	for ( var attrname in o1) {
		r[attrname] = o1[attrname];
	}
	for ( var attrname in o2) {
		r[attrname] = o2[attrname];
	}
	return r;
}

/**
 * Retrieve GET parameter's value from query.
 */
function findGetParameter(name) {
	var r = null, tmp = [];
	var items = location.search.substr(1).split('&');
	for (var index = 0; index < items.length; index++) {
		tmp = items[index].split('=');
		if (tmp[0] === name) {
			r = decodeURIComponent(tmp[1]);
		}
	}
	return r;
}

// Usage: i18n.get('key')
var i18n = new Localizer(findGetParameter('lang'));
