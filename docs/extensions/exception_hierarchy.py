                                                                     # SPDX-License-Identifier: MIT
                                                                 from __future__ import annotations
                                                                                                   
                                                                   from typing import TYPE_CHECKING
                                                                                                   
                                                                         from docutils import nodes
                                                         from docutils.parsers.rst import Directive
                                                                                                   
                                                                                  if TYPE_CHECKING:
                                                          from sphinx.application import Sphinx    
                                                 from sphinx.writers.html import HTMLTranslator    
                                                                                                   
                                                        from ._types import SphinxExtensionMeta    
                                                                                                   
                                                                                                   
                                           class exception_hierarchy(nodes.General, nodes.Element):
                                                                                           pass    
                                                                                                   
                                                                                                   
             def visit_exception_hierarchy_node(self: HTMLTranslator, node: nodes.Element) -> None:
              self.body.append(self.starttag(node, "div", CLASS="exception-hierarchy-content"))    
                                                                                                   
                                                                                                   
            def depart_exception_hierarchy_node(self: HTMLTranslator, node: nodes.Element) -> None:
                                                                   self.body.append("</div>\n")    
                                                                                                   
                                                                                                   
                                                      class ExceptionHierarchyDirective(Directive):
                                                                             has_content = True    
                                                                                                   
                                                                                 def run(self):    
                                                                  self.assert_has_content()        
                                        node = exception_hierarchy("\n".join(self.content))        
                           self.state.nested_parse(self.content, self.content_offset, node)        
                                                                              return [node]        
                                                                                                   
                                                                                                   
                                                     def setup(app: Sphinx) -> SphinxExtensionMeta:
                                                                                  app.add_node(    
exception_hierarchy, html=(visit_exception_hierarchy_node, depart_exception_hierarchy_node)        
                                                                                              )    
                          app.add_directive("exception_hierarchy", ExceptionHierarchyDirective)    
                                                                                                   
                                                                                       return {    
                                                                "parallel_read_safe": True,        
                                                               "parallel_write_safe": True,        
                                                                                              }    