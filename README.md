#CoNLL checker

Check the validity of CoNLL files and filter out the valid sentences.

##How to use it

    $ python check_conll.py ./conll_archive.conll
    866285 ** wrong ID format ** ['11', 'di', 'di', 'E', 'E', '_', '8', 'comp']
    110747349 ** wrong ID format ** ['7', 'and', 'and', 'S', 'SW', 'num=n|gen=n', '6', 'mod']
    127525027 ** wrong HEAD content ** ['4', '(', '(', 'F', 'FB', '_', '6', 'punc']
    145519895 ** wrong ID format ** ['18', '170', '170', 'N', 'N', '_', '17', 'mod']
    145520165 ** wrong ID format ** ['15', '59', '59', 'N', 'N', '_', '14', 'mod']
    145526168 ** wrong HEAD content ** ['1', 'List', 'List', 'S', 'SP', '_', '15', 'mod']
    $

It will show a report (line number, type of error, parsed line) and produce a file called conll_archive.conll.filtered which contains only valid CoNLL sentences.
The script check for the following requirements:
* 8 or 10 tab separated fields
* not broken IDs
* legitimate HEAD references
* valid content for each field

##License

(GLP v2)

Copyright (c) 2012 Michele Filannino, <http://www.cs.man.ac.uk/~filannim/>.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

##Contact
- Email: filannim@cs.man.ac.uk
- Web: http://www.cs.man.ac.uk/~filannim/