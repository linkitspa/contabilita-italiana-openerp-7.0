<!DOCTYPE html SYSTEM "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
    <head>
     <style type="text/css">
      
      .overflow_ellipsis {
                text-overflow: ellipsis;
                overflow: hidden;
                white-space: nowrap;
            } 
              
             ${css}
       div.breakbefore {page-break-before:always;
	color: silver}
    </style>
    </head>
     <% import datetime %>
    <body>
    <% setLang("it_IT") %>
    <% primo = True %>

    %for object in objects :
        %if not primo:
            <div class="breakbefore">&nbsp;</div> 
        %endif
    
       <% Compenso_lordo=0 %>
       <% IVA=0 %>
       <% Somme_n_sogg=0 %>
       <% Cassa_prev=0 %>
       <% Provv_n_sogg=0 %>
       <% Imponibile=0 %>
       <% Aliquota=0 %>
       <% Rit_operata=0 %>
       <% Rit_sospesa=0 %>
       
       
        <br><br>
        <table width="1080px;" >
        <tbody>
            <tr>
                <td width="540px">&nbsp;</td> 
                <td width="540px">
                    ${object.name}<br>
                    ${object.street}<br>
                    ${object.zip} ${object.city} ${object.province.name}
                </td> 
            </tr>
        </tbody>
        </table>   
        <br><br>      
        <div class="act_as_table list_table" style="width: 1080px; margin-top: 2px;">
            <div class="act_as_tbody " style="width: 1080px;" >   
                <div class="act_as_row lines" style="width: 1080px;">  
                   <div class="act_as_cell" style="width: 1080px;">
                        DATI IDENTIFICATI DEL SOGGETTO PERCIPIENTE<br>
                        Percipiente <b>${object.name}</b><br>
                        Nato a <b>
                        %if object.birthcity.name:
                            ${object.birthcity.name} 
                        %else:    
                            &nbsp; 
                        %endif
                        </b> il <b> 
                         %if object.birthdate:
                            ${object.birthdate} 
                        %else:    
                            &nbsp; 
                        %endif
                        </b><br>
                        Residente a <b>${object.city} (${object.province.name}) ${object.street}</b><br>
                        Codice fiscale<b> 
                         %if object.fiscalcode:
                            ${object.fiscalcode}
                        %else:    
                            &nbsp; 
                        %endif
                        </b>
                    
                        <br><br>
                        Per gli adempimenti previsti dalle vigenti norme tributarie, si attesta che al percipiente su indicato sono stati  corrsiposti per l'anno ${anno} i seguenti compensi:
                        <BR><BR>
                   </div>
                </div>
            </div>
        </div>         
        <div class="act_as_table list_table" style="width: 1080px; margin-top: 2px;">
            <div class="act_as_tbody " style="width: 1080px;" >   
                 <div class="act_as_row lines labels" style="width: 1080px;">  
                     <div class="act_as_cell" style="width: 50px;">Trib.</div>
                     <div class="act_as_cell" style="width: 110px;">Causale</b></div>
                     <div class="act_as_cell amount" style="width: 95px;">Compenso<br>lordo</div>
                     <div class="act_as_cell amount" style="width: 95px;">I.V.A.</div>
                     <div class="act_as_cell amount" style="width: 95px;">Somme n/sogg.</div>
                     <div class="act_as_cell amount" style="width: 95px;">Cassa<br>prev.</div>
                     <div class="act_as_cell amount" style="width: 95px;">Provv.<br>n/sogg</div>
                     <div class="act_as_cell amount" style="width: 95px;">Imponibile </div>
                     <div class="act_as_cell amount" style="width: 85px;">Aliquota</div>
                     <div class="act_as_cell amount" style="width: 95px;">Rit.<br>operata</div>
                     <div class="act_as_cell amount" style="width: 70px;">Rit.<br>sospesa</div>
                 </div>
            </div>
        </div>
    
        %for line in lines(object) :
        <div class="act_as_table list_table" style="width: 1080px; margin-top: 2px;">
            <div class="act_as_tbody " style="width: 1080px;" >   
                 <div class="act_as_row lines" style="width: 1080px;">  
                     <div class="act_as_cell" style="width: 50px;">${object.codice_tributo.name}</div>
                     <div class="act_as_cell" style="width: 110px;">${object.codice_tributo.desc}</div>
                     <div class="act_as_cell amount" style="width: 95px;">
                        %if (line['Compenso_lordo'])>0:
                            ${formatLang(line['Compenso_lordo'])}
                        %else:
                            &nbsp; 
                        %endif       
                     </div>
                     <div class="act_as_cell amount" style="width: 95px;">
                        %if (line['IVA'])>0:
                            ${formatLang(line['IVA'])}
                        %else:
                            &nbsp;
                        %endif       
                     </div>
                     <div class="act_as_cell amount" style="width: 95px;">
                        %if (line['Somme_n_sogg'])>0:
                            ${formatLang(line['Somme_n_sogg'])}
                        %else:
                            &nbsp; 
                        %endif       
                     </div>
                     <div class="act_as_cell amount" style="width: 95px;">
                        %if (line['Cassa_prev'])>0: 
                            ${formatLang(line['Cassa_prev'])}
                        %else:
                            &nbsp; 
                        %endif       
                     </div>
                     <div class="act_as_cell amount" style="width: 95px;">
                        %if (line['Provv_n_sogg'])>0: 
                            ${formatLang(line['Provv_n_sogg'])}
                        %else:
                            &nbsp; 
                        %endif       
                     </div>
                     <div class="act_as_cell amount" style="width: 95px;">
                        %if (line['Imponibile'])>0:
                            ${formatLang(line['Imponibile'])}
                        %else:
                            &nbsp; 
                        %endif       
                      </div>
                     <div class="act_as_cell amount" style="width: 85px;">${object.codice_tributo.aliquota}</div>
                     <div class="act_as_cell amount" style="width: 95px;">
                        %if (line['Rit_operata'])>0:
                            ${formatLang(line['Rit_operata'])}
                        %else:
                            &nbsp;
                        %endif    
                     </div>
                     <div class="act_as_cell amount" style="width: 70px;">
                         %if (line['Rit_sospesa'])>0:
                             ${formatLang(line['Rit_sospesa'])}
                         %else:
                            &nbsp;
                         %endif   
                     </div>
                 </div>
            </div>
        </div>
        
       <% Compenso_lordo += line['Compenso_lordo'] %>
       <% IVA += line['IVA']  %>
       <% Somme_n_sogg += line['Somme_n_sogg']  %>
       <% Cassa_prev += line['Cassa_prev']  %>
       <% Provv_n_sogg+= line['Provv_n_sogg']  %>
       <% Imponibile += line['Imponibile']  %>
       <% Rit_operata += line['Rit_operata']  %>
       <% Rit_sospesa += line['Rit_sospesa']  %>
                   
        %endfor 
        <div class="act_as_table list_table" style="width: 1080px; margin-top: 2px;">
            <div class="act_as_tbody " style="width: 1080px;" >   
                 <div class="act_as_row lines" style="width: 1080px;">  
                     <div class="act_as_cell" style="width: 50px;">&nbsp;</div>
                     <div class="act_as_cell" style="width: 110px;">Totali</div>
                     <div class="act_as_cell amount" style="width: 95px;">
                         %if Compenso_lordo>0:
                            ${formatLang(Compenso_lordo)}
                         %else:
                            &nbsp;   
                         %endif   
                     </div>
                     <div class="act_as_cell amount" style="width: 95px;">
                         %if IVA>0:
                            ${formatLang(IVA)}
                         %else:
                            &nbsp; 
                         %endif     
                     </div>
                     <div class="act_as_cell amount" style="width: 95px;">
                         %if Somme_n_sogg>0:
                             ${formatLang(Somme_n_sogg)}
                         %else:
                            &nbsp;  
                         %endif      
                     </div>
                     <div class="act_as_cell amount" style="width: 95px;">
                         %if Cassa_prev>0:
                             ${formatLang(Cassa_prev)}
                         %else:
                            &nbsp;
                         %endif       
                     </div>
                     <div class="act_as_cell amount" style="width: 95px;">
                        %if Provv_n_sogg>0: 
                            ${formatLang(Provv_n_sogg)}
                        %else:
                            &nbsp; 
                        %endif       
                     </div>
                     <div class="act_as_cell amount" style="width: 95px;">
                         %if Imponibile>0:
                             ${formatLang(Imponibile)}
                         %else:
                            &nbsp;
                         %endif       
                      </div>
                     <div class="act_as_cell amount" style="width: 85px;">&nbsp;</div>
                     <div class="act_as_cell amount" style="width: 95px;">
                         %if IVA>0:
                              ${formatLang(Rit_operata)}
                         %else:
                            &nbsp;
                         %endif    
                     </div>
                     <div class="act_as_cell amount" style="width: 70px;">
                         %if Rit_sospesa>0:
                             ${formatLang(Rit_sospesa)}
                         %else:
                            &nbsp;     
                         %endif    
                     </div>
                 </div>
            </div>
        </div>           
        <BR><BR>        
        <table width="1080px;" style="vertical-align:text-top;">
        <tbody>
            <tr>
                <td width="1080px" colspan="3">
                        DATI IDENTIFICATIVI DEL SOGGETTO EROGANTE O SOSTITUTO D'IMPOSTA
                        <BR><BR>
                </td>
              </tr>
              <tr>  
                <td width="200px" style="vertical-align:text-top;">
                        Soggetto erogante 
                    </td>
                    <td width="880px" colspan="2">

                        ${company.name or ''|entity} <br>  
                        ${company.street or ''|entity} ${company.street2 or ''|entity} <br>
                        ${company.zip or ''|entity} - ${company.city or ''|entity}
                  </td>
            </tr>
            <tr>
                    <td width="200px" >
                        Codice fiscale 
                    </td>
                    <td width="880px" colspan="2">

                        ${company.vat or ''|entity} 
                     </td>
            </tr>
            <tr>
                    <td width="200px" >
                        Registro impresa
                    </td>
                    <td width="880px" colspan="2">
 
                        ${company.company_registry or ''|entity}
                  </td>
            </tr>
            <tr>
                    <td width="200px" >
                        R.E.A. (CCIAA) 
                    </td>
                    <td width="880px" colspan="2">
 
                        ${company.rea or ''|entity}
                  </td>
            </tr>
            <tr>
                    <td width="200px" >
                        Cap.Soc 
                    </td>
                    <td width="880px" colspan="2">
 
                        ${company.capitale_sociale or ''|entity}
                  </td>
            </tr>
            <tr>
                     <td width="1080px" colspan="3">
                        <br><br>
                        L'importo delle ritenute e dei contributi previdenziali è stato versato in conformità alle disposizioni in materia.
                        <br><br>
                        Compensi ${anno}
                        <br><br>
                    </td>
            </tr>
                 <tr>
                    <td width="200px" >
                          
                          ${time.strftime('%d/%m/%Y', time.strptime(footer_date, '%Y-%m-%d'))} 
                          <br>          
                          -------------------<br>          
                          Data 
                     </td>
                    <td width="880px" colspan="2">
                         ${company.name or ''|entity}<br>
                         ------------------------------------------------------------<br>
                         Timbro e firma della ditta</div>
                      </td>
            </tr>
             </tbody>
        </table>
        <% primo = False %>        
   
    %endfor

    </body>
</html>
