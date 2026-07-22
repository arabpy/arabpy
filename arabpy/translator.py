"""
Tokenizer-based translator for ArabPy.

This module provides a sophisticated translator that uses Python's tokenizer
to preserve identifiers, strings, and comments while translating language
constructs and library identifiers.
"""

import tokenize
import io
import token
import keyword
from typing import List, Tuple, Optional
from .dictionary import ARABIC_TRANSLATIONS, ARABIC_TO_PYTHON


class ArabPyTranslator:
    """
    A tokenizer-based translator that converts between Python and Arabic.
    
    This translator preserves:
    - Variable names (user-defined identifiers)
    - Function names (user-defined)
    - Class names (user-defined)
    - String literals
    - Comments
    
    Only language constructs and library identifiers are translated.
    """
    
    def __init__(self):
        """Initialize the translator."""
        self.python_to_arabic = ARABIC_TRANSLATIONS
        self.arabic_to_python = ARABIC_TO_PYTHON
        
    def to_arabic(self, source_code: str) -> str:
        """
        Translate Python source code to Arabic.
        
        Args:
            source_code: Python source code to translate
            
        Returns:
            Translated source code with Arabic keywords and identifiers
        """
        return self._translate(source_code, self.python_to_arabic)
    
    def to_python(self, source_code: str) -> str:
        """
        Translate Arabic source code back to Python.
        
        Args:
            source_code: Arabic source code to translate
            
        Returns:
            Translated source code with Python keywords and identifiers
        """
        return self._translate(source_code, self.arabic_to_python)
    
    def _translate(self, source_code: str, translation_dict: dict) -> str:
        """
        Internal translation method using tokenizer.
        
        Args:
            source_code: Source code to translate
            translation_dict: Dictionary to use for translation
            
        Returns:
            Translated source code
        """
        try:
            # Tokenize the source code
            tokens = self._get_tokens(source_code)
            
            # Process tokens and build translated tokens
            translated_tokens = []
            in_fstring = False
            
            for tok in tokens:
                # Check if we're entering an f-string
                if tok.type == token.STRING and tok.string.startswith(('f"', "f'")):
                    in_fstring = True
                
                # Translate the token
                # Don't translate names inside f-strings
                if in_fstring and tok.type == token.NAME:
                    translated_tokens.append(tok)
                else:
                    translated_string = self._translate_token(tok, translation_dict)
                    # Create new token with translated string
                    translated_tokens.append(tokenize.TokenInfo(
                        type=tok.type,
                        string=translated_string,
                        start=tok.start,
                        end=tok.end,
                        line=tok.line
                    ))
                
                # Check if we're exiting an f-string
                if tok.type == token.STRING and tok.string.startswith(('f"', "f'")):
                    in_fstring = False
            
            # Use tokenize.untokenize to properly reconstruct the code
            result = tokenize.untokenize(translated_tokens)
            if isinstance(result, bytes):
                result = result.decode('utf-8')
            
            return result
            
        except (tokenize.TokenError, IndentationError, SyntaxError):
            # If tokenization fails, fall back to word-based translation
            return self._fallback_translation(source_code, translation_dict)
    
    def _get_tokens(self, source_code: str) -> List[tokenize.TokenInfo]:
        """
        Get tokens from source code using Python's tokenizer.
        
        Args:
            source_code: Source code to tokenize
            
        Returns:
            List of tokens
        """
        source_bytes = source_code.encode('utf-8')
        source_io = io.BytesIO(source_bytes)
        
        tokens = []
        for tok in tokenize.tokenize(source_io.readline):
            # Skip ENDMARKER and encoding tokens
            if tok.type != token.ENDMARKER and tok.type != tokenize.ENCODING:
                tokens.append(tok)
        
        return tokens
    
    def _translate_token(self, tok: tokenize.TokenInfo, translation_dict: dict) -> str:
        """
        Translate a single token based on its type.
        
        Args:
            tok: Token to translate
            translation_dict: Dictionary to use for translation
            
        Returns:
            Translated token string
        """
        token_string = tok.string
        
        # Don't translate strings, comments, or certain operators
        if tok.type in (token.STRING, token.COMMENT, token.NEWLINE, token.INDENT, 
                       token.DEDENT, token.NL, token.NEWLINE):
            return token_string
        
        # Translate names (identifiers)
        if tok.type == token.NAME:
            # Check if this is a Python keyword
            if keyword.iskeyword(token_string):
                return translation_dict.get(token_string, token_string)
            # Check if this is a library identifier that should be translated
            if token_string in translation_dict:
                return translation_dict[token_string]
            # Otherwise, preserve the identifier (user-defined)
            return token_string
        
        # Translate operators if they have logical names
        if tok.type == token.OP:
            return translation_dict.get(token_string, token_string)
        
        # For all other tokens, preserve as-is
        return token_string
    
    def _fallback_translation(self, source_code: str, translation_dict: dict) -> str:
        """
        Fallback translation method for when tokenization fails.
        
        This method uses a more conservative word-based approach.
        
        Args:
            source_code: Source code to translate
            translation_dict: Dictionary to use for translation
            
        Returns:
            Translated source code
        """
        # Sort keys by length (longest first) to avoid partial matches
        sorted_keys = sorted(translation_dict.keys(), key=len, reverse=True)
        
        result = source_code
        for key in sorted_keys:
            # Only translate if it's a standalone word (not part of a larger identifier)
            # This is a simple heuristic - the tokenizer approach is preferred
            import re
            pattern = r'\b' + re.escape(key) + r'\b'
            result = re.sub(pattern, translation_dict[key], result)
        
        return result
    
    def translate_file(self, input_path: str, output_path: str, to_arabic: bool = True):
        """
        Translate a file from Python to Arabic or vice versa.
        
        Args:
            input_path: Path to input file
            output_path: Path to output file
            to_arabic: If True, translate Python to Arabic; if False, translate Arabic to Python
        """
        with open(input_path, 'r', encoding='utf-8') as f:
            source_code = f.read()
        
        if to_arabic:
            translated = self.to_arabic(source_code)
        else:
            translated = self.to_python(source_code)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(translated)
    
    def translate_and_execute(self, source_code: str, to_arabic: bool = True) -> any:
        """
        Translate source code and execute it.
        
        Args:
            source_code: Source code to translate and execute
            to_arabic: If True, source is Arabic and should be translated to Python first
            
        Returns:
            Result of execution
        """
        if to_arabic:
            python_code = self.to_python(source_code)
        else:
            python_code = source_code
        
        # Execute the translated code
        namespace = {}
        exec(python_code, namespace)
        return namespace
    
    def get_translation_stats(self, source_code: str, to_arabic: bool = True) -> dict:
        """
        Get statistics about what would be translated in the source code.
        
        Args:
            source_code: Source code to analyze
            to_arabic: Direction of translation
            
        Returns:
            Dictionary with translation statistics
        """
        translation_dict = self.python_to_arabic if to_arabic else self.arabic_to_python
        
        try:
            tokens = self._get_tokens(source_code)
            translated_count = 0
            total_tokens = 0
            translated_items = []
            
            for tok in tokens:
                if tok.type == token.NAME:
                    total_tokens += 1
                    if tok.string in translation_dict:
                        translated_count += 1
                        translated_items.append({
                            'original': tok.string,
                            'translated': translation_dict[tok.string],
                            'type': 'keyword' if keyword.iskeyword(tok.string) else 'name'
                        })
            
            return {
                'total_tokens': total_tokens,
                'translated_count': translated_count,
                'translation_percentage': (translated_count / total_tokens * 100) if total_tokens > 0 else 0,
                'translated_items': translated_items
            }
        except:
            return {
                'total_tokens': 0,
                'translated_count': 0,
                'translation_percentage': 0,
                'translated_items': [],
                'error': 'Could not tokenize source code'
            }
